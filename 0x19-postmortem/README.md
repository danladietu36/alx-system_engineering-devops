


Top tech requests failure report
two days ago, it was reported that the Top tech website was returning 500 Error on all requests made on the website routes, signifying that all the services were down. 90% of the users were affected. The root cause was the failure of our master server web-01.

Timeline
The error was realized on Thursday 15th June, 2023 at 1200 hours (West Africa Time) when our Site Reliability Engineer, Mr Justice saw the master server lagging in speed. Our engineers on call disconnected the master server web-01 for further system analysis and channelled all requests to the client server web-02. Theywere able to find the cause and solved the problem on Friday 16th June 2023 at 300 hours (West Africa Time).

Root cause and resolution
The Top tech website is served by 2 ubuntu cloud servers. The master server web-01 was connected to serve all requests. Connsequently, it stopped functioning due to memory outageresulting from too many requests. The mistake happened during the previous test, the client server web-02 was disconnected temporarily for testing and was not connected to the load balancer afterwards.

The issue was solved when master server was temporarily disconnected for memory clean-up and then connected back to the loadbalancer. Again, the website was up and both master and client server started receiving requests according to the load balancer algorithm.

Measures Against Such Problem inthe Future
Choosing a good and efficient loadbalancing algorithm for your programs
Keeping an eye on your servers to ensure they are running properly
Having an extra back-up servers to prevent your program from completely going offline during an issue
