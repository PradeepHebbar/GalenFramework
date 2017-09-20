package com.brillio.utility;
import com.galenframework.testng.GalenTestNgTestBase;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.testng.annotations.DataProvider;

import java.util.List;

import static java.util.Arrays.asList;

public abstract class galenTestBase extends GalenTestNgTestBase {
	 static public WebDriver driver;

    /* (non-Javadoc)
     * @see com.galenframework.support.GalenJavaTestBase#createDriver(java.lang.Object[])
     */
    @Override
    public WebDriver createDriver(Object[] args) {
    	 TestDevice testDevice = (TestDevice)args[0];
    	 String deviceType = testDevice.device();
    	String browserType = testDevice.getBrowser();
    	Dimension dimension =  testDevice.getScreenSize();
    	String URL = testDevice.getURL();
    	
    	if(deviceType.toLowerCase().equals("desktop")){
    	
    	switch(browserType){
    	case "chrome": 
    		System.setProperty("webdriver.chrome.driver","drivers\\chromedriver.exe");
    		driver = new ChromeDriver();
    		break;
    	
    	case "firefox":
    		System.setProperty("webdriver.gecko.driver","drivers\\geckodriver.exe");
    		driver = new FirefoxDriver();
    		break;
    		
    	case "IE":
    		System.setProperty("webdriver.ie.driver","drivers\\IEDriverServer.exe");
    		driver = new InternetExplorerDriver();
    		break;
    	}
    	if(dimension!=null){
    		driver.manage().window().setSize(dimension);
    	}else{
    		driver.manage().window().maximize();
    	}
    	}
    	load(driver,URL);
        return driver;
    }

    /**
     * @return
     */
    @DataProvider(name = "devices")
    public Object [][] devices () {
        return new Object[][] {
        	
                {new TestDevice("desktop", null, asList("desktop"),"chrome","https://www.gmail.com/","desktop")},
                {new TestDevice("desktop", new Dimension(400, 600), asList("mobile"),"chrome","https://www.gmail.com/","mobile")}
        };
    }
    
    
    public void load(WebDriver driver1,String uri) {
    	driver1.get(uri);
      }
    
    public static class TestDevice {
        private final String device;
        private final Dimension screenSize;
        private final List<String> tags;
        private final String browser;
        private final String URL;
        private final String uniqueID;
        public TestDevice(String device, Dimension screenSize, List<String> tags,String browser,String URL,String uniqueID) {
            this.device = device;
            this.screenSize = screenSize;
            this.tags = tags;
            this.browser = browser;
            this.URL = URL;
            this.uniqueID = uniqueID;
        }

        public String device() {
            return device;
        }

        public Dimension getScreenSize() {
            return screenSize;
        }

        public List<String> getTags() {
            return tags;
        }

        public String getBrowser() {
			return browser;
		}

		public String getURL() {
			return URL;
		}
		
		public String uniqueID() {
			return uniqueID;
		}

		@Override
		public String toString() {
			return "TestDevice [device=" + device + ", screenSize=" + screenSize + ", tags=" + tags + ", browser="
					+ browser + ", URL=" + URL + ", uniqueID=" + uniqueID + "]";
		}

		
		
       
        
       
		
    }
    
    
    
}
