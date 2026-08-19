# Interview preparation - data engineering part 

### 1. what is hadoop mapreduce ? 
---
Hadoop mapreduce is a distributed programming model used to process very large datasets across a cluster of machines. 
<br>
it works mainly in two phase : map and reduce :
- In the Map phase, the input data is split into smaller chunks and processed in parallel by different nodes. Each mapper transforms the input into intermediate key-value pairs.
Then Hadoop performs Shuffle and Sort, where the intermediate results are grouped according to their keys.
- In the Reduce phase, reducers aggregate or process all values belonging to the same key and produce the final result.

### 2. what are the difference between relational database and HDFS ? 
---
there are 6 major categories we can define RDMBS and HDFS. they are : 
- Data Types
- Processing
- Schema on read    vs write 
- Read and write speed
- cost 
<br>

### 3. explain bigdata and explain 5vs of big data : 
--- 
bigdata is a tern for collection a large and complex datasets, that makes it to difficult processing using relational database management tools or traditional data processing applications. It is difficult capture, visualize, curate ,store , search , share transfer and analyze bigdata.
<br> IBM has defined bigdata with 5vs : 
1. value: it is good to access to bigdata but unless we turn into value it is useless. which means using bigdata adding benifits to the organizations and are they seen ROI using bigdata 
2. velocity 
3. volume 
4.variety 
5. veracity

### 4. what is hadoop and its components ? 
---
 when bigdata emerged as a problem, hadoop evolved as solution to bigdata. Apache hadoop is a framework which provides us various services or tools, to store and process bigdata
 <br>
 it helps in analyzing bigdata and making business decisions out of it, which cannot be done using traditional systems.
 <br>
 main components of hadoop are : 
 1. storage (namenode,datanode)
 2. processing framework yarn(ressource manager,node manager)

 ### 5. what are hdfs and yarn ? 
 ---
 - HDFS is the storage unit of hadoop. it is responsible for storing different kinds of data as blocks in a distributed environement 
 <br>
 it follows master and slave topology. 
 <br>
 Namenode: Namenode is the master node in the distributed environment and it maintains the metadata information for the blocks of data stored in HDFS like block location, replication factors, etc .. 
 <br>
