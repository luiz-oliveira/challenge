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

Any of the services can be hosted on AWS Cloud

![Ideal Architecture Soluction](https://github.com/luiz-oliveira/challenge/blob/master/doc/ideal_soluction.png)

---

# Actual Soluction

Because of the little time to develop, the best approach was to develop only query services with individual authentication so that we can maintain at least a basic security across all databases.

![Actual Architecture Soluction](https://github.com/luiz-oliveira/challenge/blob/master/doc/actual_soluction.png)
