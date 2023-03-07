--- To use:
---   wrk "http://127.0.0.1:5000/" -s wrk_vote.lua --latency -t 2 -c 2 -d 5s
---
--- Inspired by: https://stackoverflow.com/a/68597094/100134

--- List of rooms for randomized voting
rooms = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100'}

--- Requests submitting vote option 0
request1 = function()
    headers = {}
    headers["Content-Type"] = "application/json"
    body = '{"room_id": ' .. rooms[math.random(#rooms)] .. ',"value": 0}'
    return wrk.format("POST", "/vote", headers, body)
end

--- Requests submitting vote option 1
request2 = function()
    headers = {}
    headers["Content-Type"] = "application/json"
    body = '{"room_id": ' .. rooms[math.random(#rooms)] .. ',"value": 1}'
    return wrk.format("POST", "/vote", headers, body)
end

--- Requests submitting vote option 2
request3 = function()
    headers = {}
    headers["Content-Type"] = "application/json"
    body = '{"room_id": ' .. rooms[math.random(#rooms)] .. ',"value": 2}'
    return wrk.format("POST", "/vote", headers, body)
end

--- Control the ratio of requests
requests = {}
requests[0] = request1
requests[1] = request2
requests[2] = request3
requests[3] = request3

request = function()
    return requests[math.random(0, 3)]()
end

--- Handle error responses
response = function(status, headers, body)
    if status ~= 201 then
        io.write("------------------------------\n")
        io.write("Response with status: ".. status .."\n")
        io.write("------------------------------\n")
        io.write("[response] Body:\n")
        io.write(body .. "\n")
    end
end
