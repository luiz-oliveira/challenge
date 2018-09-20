# Challenge

Develop a soluction to work with distribucted databases and services on hight performance ambients.
Some of the data are sinsible, so the soluction should be capable of ensure the securety in specific databases and services.

# Ideal Soluction

The ideal soluction is to develop 4 diferent services tha carries specifics configurations and functions:

* Service Auth (Responsable for the althN and althZ system);
* Service A (Responsable for consults on the customer service);
* Service B (Responsable for consults on the score service);
* Service C (Responsable for consults on the tracking service);

**The service auth "works" as a proxy**
<br/>
**Only the Service A should contains sensitive data for security purposes**
<br/>
**Any of the services can be hosted on AWS Cloud**

![Ideal Architecture Soluction](https://github.com/luiz-oliveira/challenge/blob/master/doc/ideal_soluction.png)

<br/>
On the furure we should think about these applications comunicates each other directly and asynchronous, we can think about to use tornado or something like that.

**If some of these services have problems with hight concurrence, performance, or hight cost processes we could think about to use elixir and phoenix because of the Erlang VM.**

<br/>

# Actual Soluction

Because of the short time to develop, the best approach was to develop only query services with individual authentication so that we can maintain at least a basic security across all databases.

**Continuous Integration and development could be implemented individualy in the future using the Docker**

![Actual Architecture Soluction](https://github.com/luiz-oliveira/challenge/blob/master/doc/actual_soluction.png)
