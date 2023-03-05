-- To use:
--   wrk "http://127.0.0.1:5000/vote" -s wrk_vote.lua --latency -t 5 -c 20 -d 30s
wrk.method = "POST"
wrk.body = '{"room_id":3,"value":0}'
wrk.headers["Content-Type"] = "application/json"

--- TODO: multi-request random lua https://stackoverflow.com/a/68597094/100134
