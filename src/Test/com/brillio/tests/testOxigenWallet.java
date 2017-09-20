package com.brillio.tests;
import java.awt.AWTException;
import java.io.IOException;
import org.openqa.selenium.WebDriver;

import org.testng.annotations.Test;

import com.brillio.utility.galenTestBase;
import com.brillio.utility.prepareSpecs;

public class testOxigenWallet extends galenTestBase {
	static WebDriver driver;
	
	testOxigenWallet(){
		System.out.println("inside const");
	}

	@Test(dataProvider = "devices")
	public void checkLayout(TestDevice device) throws InterruptedException, IOException, AWTException {
		prepareSpecs obj = new prepareSpecs();
		driver = galenTestBase.driver;
		obj.generateSpecs(driver, driver.getCurrentUrl(), "oxigenWalletHome"+device.uniqueID());
		try {
			checkLayout("specs/outputSpecs/oxigenWalletHome"+device.uniqueID()+".spec", device.getTags());
		} catch (Exception e) {

		}
	}
}
