% The Script is used for Debug the Sending Message function
% - '192.168.31.57' is the hostIP;
% - 8000 is the hostPort;
% - 'nihao' is the example message;

import matlab.net.*
import matlab.net.http.*

r = RequestMessage;
uri = URI('http://192.168.31.57:8000/submit/nihao');
resp = send(r, uri)
status = resp.StatusCode
