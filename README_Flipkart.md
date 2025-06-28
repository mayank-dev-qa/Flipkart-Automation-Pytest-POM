
# 🛒 Flipkart Automation Testing Project

💼 Flipkart Automation Testing Project

This is a real-world automation testing project built using Selenium WebDriver, Pytest, and the Page Object Model (POM) design pattern. It simulates core user journeys on Flipkart such as login, product search, applying filters, adding to cart, and more.

####🚀 Technologies Used

🐍 Python 3.9

🧪 Pytest (Test framework)

🌐 Selenium WebDriver

🧱 Page Object Model (POM)

📊 Pytest HTML Report


#####✅ Test Cases Automated (15 Total)

##Category

Test Case Description

Login

Valid login using mobile number

Login

Invalid mobile number

Login

Blank number input

Search

Product search using keyword

Filter

Apply brand filter

Filter

Apply price filter

Filter

Brand + Price combined filter

Add to Cart

Select product, switch tab, add to cart

Add to Cart

Verify product is added

Cart

Remove product from cart

Buy Now

Click Buy Now and verify redirection

Assertion

Page title assertion

Assertion

Button text assertion

Negative Test

Add to cart without selecting product

Negative Test

Filter on empty search



#####📁 Folder Structure

Flipkart-Automation/
│
├── pages/                  # All Page Object Model classes
│   login
    Atc
    Buynowflow
    filter
    search
│
├── tests/                  # All Pytest test files
│   ├──
       login_test.py
       atc_test.py
       buynowflow_test.py
       filter_test.py
       search_test.py


├── Screenshots/            # (Optional) Screenshots

├── Bug_Report.pdf          # (Optional) Bug report

├── Test_Summary.pdf        # (Optional) Test execution summary

├── conftest.py             # Pytest fixture for browser setup

├── requirements.txt        # Python dependencies

├── report.html             # HTML test execution report

__ Test Plan               # Test plan for project

└── README.md               # This file


######🧪 How to Run

    [Clone this Repository] 

git clone https://github.com/<mayank--dev-qa>/flipkart-automation.git
cd flipkart-automation

@@@@Install Required Packages

pip install -r requirements.txt

Run the Test Suite

pytest --html=report.html


####📸 Report Preview

report.html file will be generated with detailed pass/fail status.Example:

Test Summary: 15 passed, 0 failed


####📌 Notes


Flipkart is a live production website — please avoid misuse.

OTP login step is automated only up to the OTP entry screen (no real OTP used).

This is a portfolio project meant to demonstrate automation skills using real websites.

     ####{🙋‍♂️ Author}####

Mayank Agrawal -- QA Automation Engineer | Python + Selenium + Pytest | Postman | 
Git📧 [mayank@example.com🌐](https://github.com/mayank-dev-qa) 
 LinkedIn💼
 GitHub