# A2 Architectures

## 1. Read the systems design primer thoroughly!
A data stream is a potentially unbounded sequence of events

Events in a data stream can represent monitoring data, sensor measurements, credit card 
transactions, weather station observations, online user interactions, web searches, etc. 

### What is the difference between latency and throughput?

[source](https://github.com/donnemartin/system-design-primer)

Latency indicates how long it takes for an event to be processed. Essentially, it is 
the time interval between receiving an event and seeing the effect of processing this 
event in the output.

In data streaming, latency is measured in units of time, such as milliseconds. 
Depending on the application, we might care about average latency, maximum latency, 
or percentile latency.

Throughput is a measure of the system’s processing capacity, i.e. its rate of processing. 
That is, throughput tells us how many events the system can process per time unit.

Throughput is measured in events or operations per time unit. It is important to note 
that the rate of processing depends on the rate of arrival; low throughput does 
not necessarily indicate bad performance. 

At this point, it should be quite clear that latency and throughput are not independent
metrics. If events take long to travel in the data processing pipeline, we cannot easily 
ensure high throughput. Similarly, if a system’s capacity is small, events will be 
buffered and have to wait before they get processed.

**Little conclusion**: as big as possible throughput and acceptable latency.

### What would you design a AP or a CP System?

**CP - consistency and partition tolerance**

Waiting for a response from the partitioned node might result in a timeout error. 

**AP - availability and partition tolerance**

Responses return the most recent version of the data available on a node, which 
might not be the latest. Writes might take some time to propagate when the partition 
is resolved.

**Conclusion**: it depends, CP is a good choice if business needs require atomic reads and writes.
AP is a good choice if the business needs allow for eventual consistency or when 
the system needs to continue working despite external errors.

### What is Replication, Failover and how does Redis replication work?

[source 1](https://docs.oracle.com/cd/E13222_01/wls/docs90/cluster/failover.html)
[source 2](https://redis.io/topics/replication)

**Replication** is a process of replication session data from one server to another 
within a cluster.

**Failover** is a process when a server within a cluster fails.

When a server within a cluster fails, the local **load balancer** is responsible for 
transferring the request to other servers within a cluster.

At the base of Redis replication (excluding the high availability features provided 
as an additional layer by Redis Cluster or Redis Sentinel) there is a very simple 
to use and configure leader follower (master-slave) replication: it allows replica 
Redis instances to be exact copies of master instances. 

**Conclusion**: Redis uses a master-slave replication.

### What would be the perfect database / database model for your SWT PET project if you would have to scale large and having some 10.000 clients?

[My Pet Project](https://github.com/ElijahOzhmegov/Smake-Snake-AI-)

I have doubt about the need in a database for my PET project. 
But if had to create one, firstly I would create it for keeping
players' scores, then I would use the cheapest one, I guess for me 
it would be a master-slave replication.


### What are the advantages and disadvantages of (web) caching?

**Pros**
* Caching improves page load times and can reduce the load on your servers and databases.
* Databases often benefit from a uniform distribution of reads and writes across its 
  partitions. Popular items can skew the distribution, causing bottlenecks. Putting a 
  cache in front of a database can help absorb uneven loads and spikes in traffic.
* Web servers can also cache requests, returning responses without having to 
  contact application servers.

**Cons**
* Need to maintain consistency between caches and the source of truth such as the database through cache invalidation.
* Cache invalidation is a difficult problem, there is additional complexity associated with when to update the cache.
* Need to make application changes such as adding Redis or memcached.

### What is the difference between RPC and Rest?

**RPC** (Remote procedure call) is a request-response protocol.
A client causes a procedure to execute on a different address space, usually a remote 
server. The procedure is coded as if it were a local procedure call, abstracting away 
the details of how to communicate with the server from the client program. Remote calls
are usually slower and less reliable than local calls so it is helpful to distinguish 
RPC calls from local calls.

**REST** (Representational state transfer) is an architectural style enforcing a client/server model where the client acts 
on a set of resources managed by the server. The server provides a representation of 
resources and actions that can either manipulate or get a new representation of 
resources. All communication must be stateless and cacheable.

**Conclusion**: RPC is about do one job, but well. When REST API’s only concern is the
data that belongs to that specific domain.

### How many cores does the Stackoverflow Servers have, with what chip Hz and how many MB L2 cache?

According to [this source](https://nickcraver.com/blog/2016/03/29/stack-overflow-the-hardware-2016-edition/).
* SQL Servers (Stack Overflow Cluster) | Dual E5-2697v2 Processors (12 cores @2.7–3.5GHz each) | 12 x 256 KB 8-way set
* SQL Servers (Stack Exchange “…and everything else” Cluster) | Dual E5-2667v3 Processors (8 cores @3.2–3.6GHz each) | 8 x 256 KB 8-way set
* Web Servers | Dual E5-2690v3 Processors (12 cores @2.6–3.5GHz each) | 12 x 256 KB 8-way set

## 2) GPU (1 page): Do a little research on GPU &TPU.

### How would you get a simple GPU "Hello World" Example run on Google or AWS? (theoretically. Not practically!)

1. Via [colab.research.google.com](https://colab.research.google.com/notebooks/intro.ipynb)
2. Like [this](TensorFlow_with_GPU.ipynb)
