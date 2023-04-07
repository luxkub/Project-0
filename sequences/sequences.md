@startuml Checkout
actor Customer
boundary "Register" as register
control "Checkout" as checkout
control "Payment" as pay
Customer -> register: Checkout
activate register
register -> Payment: payment(cost, payment)
activate pay
pay --> Register: True
deactivate pay
register -> Checkout: add_new_checkout(cost, payment)
activate checkout
checkout --> register: None
deactivate checkout
register -> register: redirect to home page
deactivate register
@enduml

@startuml Buyback
actor Customer
boundary "Register" as register
control "VideoGame" as game
control "Payment" as pay
Customer -> register: Buyback
activate register
register -> Payment: payment(credit, payment)
activate pay
game --> Register: True
deactivate game
register -> Buyback: add_new_game(credit, payment)
activate videogame
videogame --> register: None
deactivate videogame
register -> register: redirect to home page
deactivate register
@enduml

@startuml AddVideoGameObject
actor Staff
boundary "InventorySize" as iSize
control "addItem" as addI
control "Inventory" as Inventory
Staff -> iSize: AddVideoGameObject
activate isize
iSize -> addI: addItem(cost, quantity)
activate addI
Inventory --> iSize: True
deactivate Inventory
iSize -> AddVideoGameObject: add_new_videogame(cost, quantity)
activate addI
addI --> iSize: None
deactivate addI
iSize -> iSize: redirect to home page
deactivate iSize
@enduml

@startuml moreInfo
actor Customer
boundary "noItem" as noItem
control "VideoGame" as item
control "Description" as desc
Customer -> noItem: moreInfo
activate noItem
noItem -> desc: add_desc(desc, Inventory)
activate desc
desc --> noItem: True
deactivate desc
noItem -> item: add_new_item(item, desc)
activate item
item --> noItem: None
deactivate item
noItem -> noItem: redirect to home page
deactivate noItem
@enduml

@startuml InventoryList
actor Staff
boundary "Inventory Size" as iSize
control "Item" as item
control "Description" as descc
Staff -> iSize: Login
activate iSize
iSize -> desc: addDescription(price, quantity)
activate desc
desc --> iSize: True
deactivate desc
iSize -> item: add_new_item(desc)
activate item
item --> iSize: None
deactivate item
iSize -> iSize: redirect to home page
deactivate iSize
@enduml

@startuml removeInventory
actor Staff
boundary "Inventory" as iSize
control "Item" as item
control "InventoryisnotEmpty" as iempty
Staff -> iSize: Login
activate iSize
iSize -> iempty: login_pipeline(username, password)
activate iempty
iempty --> iSize: True
deactivate iempty
iSize -> item: add_new_session(username, db)
activate item
item --> iSize: None
deactivate item
iSize -> iSize: redirect to home page
deactivate iSize
@enduml
