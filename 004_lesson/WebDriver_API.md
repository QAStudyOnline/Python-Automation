# WebDriver API

## Locators

#### To find single element:

```
* driver.find_element_by_id
* driver.find_element_by_name
* driver.find_element_by_xpath
* driver.find_element_by_link_text
* driver.find_element_by_partial_link_text
* driver.find_element_by_tag_name
* driver.find_element_by_class_name
* driver.find_element_by_css_selector
```

#### To find multiple elements (these methods will return a list):

```
* driver.find_elements_by_name
* driver.find_elements_by_xpath
* driver.find_elements_by_link_text
* driver.find_elements_by_partial_link_text
* driver.find_elements_by_tag_name
* driver.find_elements_by_class_name
* driver.find_elements_by_css_selector
```

## Methods

```
driver.get(some site url)
driver.quit()
driver.close()
driver.title 
driver.maximize_window()
driver.execute_script(javascript that should be executed)
driver.switch_to.frame(name attribute on iframe element)
```

## Waiters

```
driver.implicitly_wait(10)
```

```
WebDriverWait(driver,10)
.until(expected_conditions.visibility_of_element_located(<LOCATOR>>))
```
