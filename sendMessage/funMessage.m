function [resp, status] = funMessage(msg)
    % Send [msg] to the Django host at
    % 192.168.31.57:8000
    % The function will report resp and status as running
    import matlab.net.*
    import matlab.net.http.*

    r = RequestMessage;
    uri = URI(['http://192.168.31.57:8000/submit/', msg]);
    resp = send(r, uri)
    status = resp.StatusCode
end
