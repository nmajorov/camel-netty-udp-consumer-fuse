##Example of netty udp consumer for the JBoss Fuse


Build it with a command:
	
			mvn clean install


start jboss fuse (tested with 6.1) :


			JBossFuse:karaf@root> features:addurl mvn:biz.majorov.camel/nm-camel-udp-fuse/1.0/xml/features

			JBossFuse:karaf@root> features:install nm-udp-fuse

See in the logs if netty consumer is started:

			
			JBossFuse:karaf@root> log:tail


		Total 1 routes, of which 1 is started.
		2014-06-12 23:57:28,400 | INFO  | xtenderThread-12 | OsgiSpringCamelContext           | ?                                   ? | 142 - org.apache.camel.camel-core - 2.12.0.redhat-610379 | Apache Camel 2.12.0.redhat-610379 (CamelContext: camel-6) started in 0.088 seconds
		2014-06-12 23:57:28,409 | INFO  | xtenderThread-12 | OsgiBundleXmlApplicationContext  | ?                                   ? | 121 - org.apache.servicemix.bundles.spring-context - 3.2.8.RELEASE_1 | Publishing application context as OSGi service with properties {org.springframework.context.service.name=biz.majorov.camel.nm-camel-udp-fuse, Bundle-SymbolicName=biz.majorov.camel.nm-camel-udp-fuse, Bundle-Version=1.0.0}
		2014-06-12 23:57:28,419 | INFO  | xtenderThread-12 | ContextLoaderListener            | ?                                   ? | 145 - org.springframework.osgi.extender - 1.2.1 | Application context successfully refreshed (OsgiBundleXmlApplicationContext(bundle=biz.majorov.camel.nm-camel-udp-fuse, config=osgibundle:/META-INF/spring/*.xml))
		





Curerntly it's listen on the localhost and port 1234. To use multicast ip and other port please change the **features.xml** file.
I test it with ruby command, but you can send some text with any programm on port 1234 and  see the output in JBoss Fuse log.


to test with ruby (ruby 1.9.x or 2.x versions should be installed) type the following command:


			nikolajrovsmbp4:~ nmajorov$ irb 
			2.1.1 :001 > require 'socket'
			 => true 
			2.1.1 :002 > s = UDPSocket.new
			 => #<UDPSocket:fd 9> 
			2.1.1 :003 > s.send("hello",0,'localhost',1234)
			 => 5 
