UPDATE cookie_profile
SET cookie = ?, last_run_time = (CURRENT_TIMESTAMP), run_count = run_count + 1
WHERE id = ?;