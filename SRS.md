# Software Requirements Specification Document

## Group Members

* [Winnie Kubuanu](mailto:ekubuanu@uncc.edu)
* [Mack Larson](mailto:clarson9@uncc.edu)
* [Zachary Turnmire](mailto:zturnmir.uncc.edu)

## Revisions

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |
|1.0| 03/30/23 | Initial draft | [Mack Larson](mailto:clarson9@uncc.edu) | [Mack Larson](mailto:clarson9@uncc.edu) |
| 1.0 | 03/22/23 | Initial draft | [Winnie Kubuanu](mailto:ekubuanu@uncc.edu) | [Winnie Kubuanu](mailto:ekubuanu@uncc.edu) |
| 1.0 | 03/30/23 | Initial draft | [Zachary Turnmire](mailto:zturnmir.uncc.edu) | [Zachary Turnmire](mailto:zturnmir.uncc.edu) |

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction

Our project is a videogame store where users will be able to shop through a listed inventory that states the quanity and price of available videogames. The customer will able to view the quantity and price of all items available and will be able to shop for multiple items at a time. When the inventory of an item hits 0, staff of the store will be able to remove the object from inventory. Customers will be able to checkout using their card information. 

## Requirements


* **REQ-7:** Video game Object
  * **Description:** A Video game Object that stores a Price, a inventory size, A image, and the name of the Video game
  * **Type:** Functional
  * **Priority:** 3
  * **Rationale:** This requirement stores inventory, as well as the display capabilities and prices
  * **Testing:** We would write tests to check price, inventory, and images.  

* **REQ-8:** Checkout
  * **Description:** A Checkout process where a person can buy the items in their shopping cart
  * **Type:** Functional
  * **Priority:** 1
  * **Rationale:** The people need to be able to buy whatever they want to get from the stole
  * **Testing:** We would write tests to check that inventory decreases, the customer gets their card charged, and the shopping cart gets emptied

* **REQ-9:** Error Messages
  * **Description:** Clear and consise error messages to tell the client what they did wrong
  * **Type:** Functional
  * **Priority:** 5
  * **Rationale:** These error messages would help the client know what they should do right.
  * **Testing:** We would write tests to check error messages are thrown when someone enters something we dont want into a field  

* **REQ-4** Searching
  * **Description:** A search function that makes it simple and quick for users to find content should be available on the website.
  * **Type:** `Functional`
  * **Priority:** 1
  * **Rationale:** A search function helps users quickly find the content they're looking for instead of navigating through numerous pages or menus.
  * **Testing:** You can test the functionality of the search function by entering a search query.

* **REQ-5:** Shopping Cart
  * **Description:** A shopping cart function that enables users to add things they want to buy and determine the total cost of their transaction should be available on the website store.
  * **Type:** `Functional`
  * **Priority:** 2
  * **Rationale:** By enabling customers to quickly buy multiple items at once rather than having to check out each item separately, a shopping cart feature can boost sales.
  * **Testing:** You can test a shopping cart function by adding products, changing quantities, and removing items.

* **REQ-6** Accessibility
  * **Description:** The website's content should be easy to read and understand.
  * **Type:** `Functional`
  * **Priority:** 2
  * **Rationale:** Content that is simple to read and understand has a higher chance of generating user engagement. Users may become annoyed and leave the website if the material is unclear, hard to understand, or full of jargon, which can have an effect on engagement and conversions.
  * **Testing:** We may test this by asking a group of visitors to read the website's content and offer feedback on the text's clarity and readability.

* **REQ-1:** Inventory
  * **Description:** A list containing all items sold in the store.
  * **Type:** Functional
  * **Priority:** 1
  * **Rationale:** Inventory is important to be able to track what games are currently sold in the shop. 
  * **Testing:** Checks if the list is empty.

* **REQ-2:** Price
  * **Description:** The price of a videogame in the store. 
  * **Type:** Functional
  * **Priority:** 3
  * **Rationale:** Price is used in the checkout feature.
  * **Testing:** Checks if Price exists.
  
* **REQ-3** Quantity
  * **Description:** Stores the current quantity of a specific videogame's quanity and check if it needs removed from list.
  * **Type:** Functional
  * **Priority:** 3
  * **Rationale:** Check to see if an item needs to be removed from list.
  * **Testing:** Checks to see if inventory is less than zero.

## Constraints

 * **Project Requirements:** The website must be aesthetically pleasing  which can be difficult when there are few design resources available.

 * **Language Constraint:** For this project we are limited to using Python and Flask.

 * **Real:** We are constraned by real-world applications 

 * **Video games:** We are constraned to only selling video game objects because this is a video game store

 * **Time:** Our project is limited by time due to the School Semester.

 * **Experience:** Most members are using Python for the first Semester, so we are limited by our experience in Python.

## Use Cases

* **UC-3:** Checkout
  * **Description:** The user can start the checkout procedure, which entails providing their billing and shipping information, choosing a payment option, and reviewing their order specifics before completing the transaction.
  * **Actors:** The customer
  * **Preconditions:** The user has added an item to their cart, entered their shipping and billing information, their payment method, and submitted their payment.
  * **Postconditions:** In an online web store, processing the customer's shipping label and sending the order to the shipping carrier are among the postconditions of the checkout use case. The store may also create an order confirmation page and send the user an email of confirmation, update its inventory system, or update its inventory system. 

* **UC-5:** BuyBack
  * **Description:** A person should be able to return the games back to the store
  * **Actors:** Customer
  * **Preconditions:** Bought a game before, game is still on store
  * **Postconditions** game inventory is moved up one, and person recieves money on card used to purchase

* **UC-6:** Add video game object
  * **Description:** The ability to add a new video game product to the store
  * **Actors:** Admin
  * **Preconditions:** More then zero of the item you're trying to add, and the information for the fields
  * **Postconditions** A new item added to the store, along with description, price, and name. 

* **UC-4:** View more info
  * **Description:** A user can click on a single product to view more information, including a description.
  * **Actors:** The customer
  * **Preconditions:** The user has added an item to their cart, entered their shipping and billing information, their payment method, and submitted their payment.
  * **Postconditions:** The postconditions of the "search and browse products" use case would be the user being shown a list of products based on their search query. 

* **UC-1:** InventoryList
  * **Description:** A function to output the current inventory in the store.
  * **Actors:** Admin and customers.
  * **Preconditions:** The Inventory list must have items in it.
  * **Postconditions:** Inventory must remove items with a quantity of 0.

* **UC-2:** RemoveInventory
  * **Description:** A function that removes a item from inventory.
  * **Actors:** Admin
  * **Preconditions:** Inventory must contain an object. 
  * **Postconditions:** Object should be properly removed.


## User Stories

* **US-3:** Johnny
  * **Type of User:** `Customer`
  * **Description:** Johnny wants to quickly find the games he wants on our online store. Without encountering any navigational difficulties or technical difficulties, he plans to travel to the homepage of the online store, look for the items and add them to his cart. He will be happy with the online shopping experience and intends to return to the website for additional purchases if she can quickly and simply find all the items he wants.

* **US-5:** Checking Out of Store
  * **Type of User:** Customer
  * **Description:** Kayla is shopping for video games on the online store. She wants to be able to buy the games she has gotten and experience it without errors

* **US-6:** Adding new inventory to the store
  * **Type of User:** Admin
  * **Description:** The Admin for the store would like to be able to add new video games whenever they come in, so people can start purchasing right away

* **US-4:** Tomas
  * **Type of User:** `Customer`
  * **Description:** Tomas, a dedicated gamer, wants to browse the online store's assortment of video games fast and conveniently, view in-depth information on each game, and buy it. He anticipates a quick and easy checkout experience and intends to come back for additional purchases.

* **US-1:** RemoveInventory
  * **Type of User:** Admin
  * **Description:** Admin can use the removeInventory function to find and remove all items that have 0 inventory. All items that are removed are outputted to the admin in case of any misintended deletions.
* **US-2:** ShoppingCart
  * **Type of User:** Customers
  * **Description:** A customer can view each inventory item available and select items to add to their shopping cart. They can view their own shopping cart and the total price with tax.


## Glossary

* **Term:** Attribute
  * **Definition:** A field that contains info, mainly used in objects.
  
* **Term:** Function
  * **Definition:** A function is a website's ability to complete a particular task.

* **Term:** List
  * **Definition:** A list of objects that have their own unique attributes.
