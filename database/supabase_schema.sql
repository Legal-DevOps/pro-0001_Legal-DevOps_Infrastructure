-- ================================================
-- Legal-DevOps Infrastructure — Supabase Schema
-- Antigravity Nexus | v4.0
-- ================================================
-- Run this in Supabase SQL Editor (Dashboard → SQL Editor → New Query)

-- Enable UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ================================================
-- CASES
-- ================================================
CREATE TABLE cases (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    case_id TEXT UNIQUE NOT NULL,           -- "0001", "0002", "0003"
    title TEXT NOT NULL,
    status TEXT DEFAULT 'active',           -- active, closed, suspended
    priority TEXT DEFAULT 'normal',         -- critical, high, normal, low
    description TEXT,
    objective TEXT,
    address TEXT,
    strategy_mode TEXT,
    risks JSONB DEFAULT '[]'::jsonb,
    metadata JSONB DEFAULT '{}'::jsonb,     -- flexible extra fields
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- ================================================
-- PARTIES (participants in a case)
-- ================================================
CREATE TABLE parties (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    case_id TEXT REFERENCES cases(case_id) ON DELETE CASCADE,
    role TEXT NOT NULL,                     -- Subject, Partner, Child, Witness, Management Company
    name TEXT NOT NULL,
    citizenship TEXT,
    status TEXT DEFAULT 'active',
    contacts JSONB DEFAULT '{}'::jsonb,     -- {phone, email, address}
    document TEXT,                          -- passport / ID info
    notes TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ================================================
-- TASKS
-- ================================================
CREATE TABLE tasks (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    case_id TEXT REFERENCES cases(case_id) ON DELETE CASCADE,
    task_number INTEGER NOT NULL,           -- sequential within case
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'todo',             -- todo, in-progress, done
    priority TEXT DEFAULT 'normal',         -- critical, high, normal
    deadline DATE,
    phone TEXT,
    address TEXT,
    local_file TEXT,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(case_id, task_number)
);

-- ================================================
-- HISTORY (audit trail)
-- ================================================
CREATE TABLE history (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    case_id TEXT REFERENCES cases(case_id) ON DELETE CASCADE,
    agent TEXT DEFAULT 'System',
    event TEXT NOT NULL,
    details TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ================================================
-- CORRESPONDENCE (response tracker)
-- ================================================
CREATE TABLE correspondence (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    corr_id TEXT UNIQUE NOT NULL,           -- CORR-0003-001
    case_id TEXT REFERENCES cases(case_id) ON DELETE CASCADE,
    direction TEXT DEFAULT 'outgoing',      -- outgoing, incoming
    document TEXT NOT NULL,
    recipient TEXT,
    sent_date DATE,
    sent_via TEXT DEFAULT 'email',
    deadline_law TEXT,
    deadline_date DATE,
    status TEXT DEFAULT 'awaiting_response', -- awaiting_response, received, escalated, overdue
    response_date DATE,
    response_result TEXT,
    escalation JSONB,
    notes TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ================================================
-- DOCUMENTS (metadata for generated files)
-- ================================================
CREATE TABLE documents (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    case_id TEXT REFERENCES cases(case_id) ON DELETE CASCADE,
    filename TEXT NOT NULL,
    file_type TEXT DEFAULT 'md',            -- md, docx, pdf
    category TEXT DEFAULT 'final_output',   -- final_output, plan, raw_data, notary
    sha256 TEXT,
    size_bytes INTEGER,
    storage_path TEXT,                      -- Supabase Storage path
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ================================================
-- LAWS (legal knowledge base)
-- ================================================
CREATE TABLE laws (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    law_id TEXT UNIQUE NOT NULL,            -- "access_to_info", "family_code"
    full_name TEXT NOT NULL,
    short_name TEXT,
    number TEXT,
    date DATE,
    key_articles JSONB DEFAULT '{}'::jsonb,
    deadlines JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ================================================
-- ROW LEVEL SECURITY (RLS)
-- ================================================

-- Enable RLS on all tables
ALTER TABLE cases ENABLE ROW LEVEL SECURITY;
ALTER TABLE parties ENABLE ROW LEVEL SECURITY;
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;
ALTER TABLE history ENABLE ROW LEVEL SECURITY;
ALTER TABLE correspondence ENABLE ROW LEVEL SECURITY;
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE laws ENABLE ROW LEVEL SECURITY;

-- For now: allow all access for authenticated users
-- (can be tightened later per-role)
CREATE POLICY "Authenticated users can read all" ON cases FOR SELECT TO authenticated USING (true);
CREATE POLICY "Authenticated users can insert" ON cases FOR INSERT TO authenticated WITH CHECK (true);
CREATE POLICY "Authenticated users can update" ON cases FOR UPDATE TO authenticated USING (true);

CREATE POLICY "Authenticated users can read parties" ON parties FOR SELECT TO authenticated USING (true);
CREATE POLICY "Authenticated users can insert parties" ON parties FOR INSERT TO authenticated WITH CHECK (true);

CREATE POLICY "Authenticated users can read tasks" ON tasks FOR SELECT TO authenticated USING (true);
CREATE POLICY "Authenticated users can insert tasks" ON tasks FOR INSERT TO authenticated WITH CHECK (true);
CREATE POLICY "Authenticated users can update tasks" ON tasks FOR UPDATE TO authenticated USING (true);

CREATE POLICY "Authenticated users can read history" ON history FOR SELECT TO authenticated USING (true);
CREATE POLICY "Authenticated users can insert history" ON history FOR INSERT TO authenticated WITH CHECK (true);

CREATE POLICY "Authenticated users can manage correspondence" ON correspondence FOR ALL TO authenticated USING (true);
CREATE POLICY "Authenticated users can manage documents" ON documents FOR ALL TO authenticated USING (true);
CREATE POLICY "Anyone can read laws" ON laws FOR SELECT TO anon, authenticated USING (true);
CREATE POLICY "Authenticated users can manage laws" ON laws FOR ALL TO authenticated USING (true);

-- Service role can do everything (for Python backend)
CREATE POLICY "Service role full access cases" ON cases FOR ALL TO service_role USING (true);
CREATE POLICY "Service role full access parties" ON parties FOR ALL TO service_role USING (true);
CREATE POLICY "Service role full access tasks" ON tasks FOR ALL TO service_role USING (true);
CREATE POLICY "Service role full access history" ON history FOR ALL TO service_role USING (true);
CREATE POLICY "Service role full access correspondence" ON correspondence FOR ALL TO service_role USING (true);
CREATE POLICY "Service role full access documents" ON documents FOR ALL TO service_role USING (true);
CREATE POLICY "Service role full access laws" ON laws FOR ALL TO service_role USING (true);

-- ================================================
-- INDEXES for performance
-- ================================================
CREATE INDEX idx_tasks_case_id ON tasks(case_id);
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_tasks_deadline ON tasks(deadline);
CREATE INDEX idx_parties_case_id ON parties(case_id);
CREATE INDEX idx_history_case_id ON history(case_id);
CREATE INDEX idx_correspondence_case_id ON correspondence(case_id);
CREATE INDEX idx_correspondence_status ON correspondence(status);
CREATE INDEX idx_correspondence_deadline ON correspondence(deadline_date);
CREATE INDEX idx_documents_case_id ON documents(case_id);

-- ================================================
-- AUTO-UPDATE updated_at
-- ================================================
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER cases_updated_at BEFORE UPDATE ON cases
    FOR EACH ROW EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER tasks_updated_at BEFORE UPDATE ON tasks
    FOR EACH ROW EXECUTE FUNCTION update_updated_at();

-- ================================================
-- VIEW: overdue items (tasks + correspondence)
-- ================================================
CREATE OR REPLACE VIEW overdue_items AS
SELECT
    'task' AS item_type,
    t.case_id,
    t.task_number AS item_number,
    t.title,
    t.deadline AS deadline_date,
    (CURRENT_DATE - t.deadline) AS days_overdue,
    t.priority
FROM tasks t
WHERE t.status != 'done'
  AND t.deadline < CURRENT_DATE

UNION ALL

SELECT
    'correspondence' AS item_type,
    c.case_id,
    0 AS item_number,
    c.document AS title,
    c.deadline_date,
    (CURRENT_DATE - c.deadline_date) AS days_overdue,
    'high' AS priority
FROM correspondence c
WHERE c.status = 'awaiting_response'
  AND c.deadline_date < CURRENT_DATE

ORDER BY days_overdue DESC;

-- ================================================
-- VIEW: case summary dashboard
-- ================================================
CREATE OR REPLACE VIEW case_summary AS
SELECT
    c.case_id,
    c.title,
    c.status,
    c.priority,
    COUNT(t.id) AS total_tasks,
    COUNT(t.id) FILTER (WHERE t.status = 'done') AS done_tasks,
    COUNT(t.id) FILTER (WHERE t.status = 'in-progress') AS progress_tasks,
    COUNT(t.id) FILTER (WHERE t.status = 'todo') AS todo_tasks,
    COUNT(t.id) FILTER (WHERE t.deadline < CURRENT_DATE AND t.status != 'done') AS overdue_tasks,
    COUNT(d.id) AS document_count,
    c.updated_at
FROM cases c
LEFT JOIN tasks t ON t.case_id = c.case_id
LEFT JOIN documents d ON d.case_id = c.case_id
GROUP BY c.id, c.case_id, c.title, c.status, c.priority, c.updated_at
ORDER BY c.case_id;
