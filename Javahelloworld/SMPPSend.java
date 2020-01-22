/* Code block to send sms to a set of msisdn's by SMSProcessor */
				try {
					// new SMS
					log.debug("Collector>  Add here the sending of SMS message");

					// Input Operator logfile given
					TreeMap msisdnFileMap=new TreeMap();
					msisdnFileMap.put(new Integer(0), "examplemsisdnlist.txt");

					// expects text file with MSIDN numbers
					String msisdnFileList="";
					Object[] fileArray=msisdnFileMap.values().toArray();

					for (int i=fileArray.length-1;i>=0;i--) {
						msisdnFileList+=(String)fileArray[i];
					}
					log.debug("Collector>  New logfile list: " + msisdnFileList);

					// 2.2 Start threads for all new msisdn files
					if(fileArray.length>0){



						int bindRetries=10;
						try {
							bindRetries=Integer.parseInt(PROPS.getProperty("MAX_SMSC_BIND_RETRIES"));
						} catch (Exception e) {
							log.error("MAX_SMSC_BIND_RETRIES not defined - using 10 as default.");
						}
						int SMSCbindDelay=100;
						try {
							SMSCbindDelay=Integer.parseInt(PROPS.getProperty("SMSC_BIND_DELAY"));
						} catch (Exception e) {
							log.error("SMSC_BIND_DELAY not defined - using 100 as default.");
						}
						String smsMessage="You are now MMS capable";
						try {
							smsMessage=PROPS.getProperty("SMS_MESSAGE_TEXT");
						} catch (Exception e) {
							log.error("SMS_MESSAGE_TEXT not defined - using \"You are now MMS capable\" as default.");
						}
						int smsEncoding=0;
						try {
							smsEncoding=Integer.parseInt(PROPS.getProperty("SMS_ENCODING_STANDARD"));
						} catch (Exception e) {
							log.error("SMS_ENCODING_STANDARD not defined - using 0 as default.");
						}
						SMSProcessor[] smsProcessor = new SMSProcessor[fileArray.length];
						for (int i=fileArray.length-1;i>=0;i--) {
							log.debug("Collector>  MSISDN File to set: " + (String)fileArray[i]);
							log.debug("Collector>  bindRetries="+bindRetries+",SMSCbindDelay="+SMSCbindDelay+",smsMessage="+smsMessage+",smsEncoding="+smsEncoding);
							smsProcessor [i] = new SMSProcessor(PROPS);
							smsProcessor [i].init(bindRetries,SMSCbindDelay,smsMessage,smsEncoding);
							smsProcessor [i].setMsisdnFile((String)fileArray[i]);
						}

						// Start threads one by one
						for (int i=fileArray.length-1;i>=0;i--) {
							log.info("Start processing file: " + (String)fileArray[i]);
							smsProcessor [i].run();
							smsProcessor [i].disconnectSMSC();
							log.debug("Collector>  Processor finished. Thread ends.");
						}
					}

				} catch (Exception e) {
					log.error("ERROR:"+e.getMessage());
				}
send msisdn's */
