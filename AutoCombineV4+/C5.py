y = (30,262)
b = (30,210)
p = (87,210)
r = (145,204)
g = (145,320)

# zoom
# y = (36, 120)
# b = (36, 43)
# p = (113, 43)
# r = (190, 43)
# g = (190, 197)

actions = [
    ("utYfull",0.65,False,"click",y),
    ("wrench",0.95,False,"click",None),

    # === PICK YELLOW === 
    ("wrenched",0.9,False,"click",y),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),
    # === PICK RED === 
    ("info",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",r),
    ("close",0.9,False,"confirmer",None),
    ("RetItems",0.9,True,"if",[("close",0.9,False,"click",None)]),
    ("RetItems",0.9,False,"if",[("RetItems",0.9,False,"click",None),
                            ("Retrieve",0.9,False,"click",None),]),
    # # === PICK PINK ===
    ("info",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",p),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),
    # # === PICK BLUE ===
    ("info",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",b),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),
    # # === PICK GREEN ===
    ("info",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",g),
    ("close",0.9,False,"confirmer",None),
    ("RetItems",0.9,True,"if",[("close",0.9,False,"click",None)]),
    ("RetItems",0.9,False,"if",[("RetItems",0.9,False,"click",None),
                            ("Retrieve",0.9,False,"click",None),]),

    # === DROP YELLOW ===
    ("info",0.9,False,"confirmer",None),
    ("yellowchem",0.9,False,"click",None),
    ("pickedY",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP BLUE ===
    ("info",0.9,False,"confirmer",None),
    ("bluechem",0.9,False,"click",None),
    ("pickedB",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP PINK ===
    ("info",0.9,False,"confirmer",None),
    ("pinkchem",0.9,False,"click",None),
    ("pickedP",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # === COMBINE M === 
    ("info",0.9,False,"confirmer",None),
    ("punched",0.9,True,"if",[("punch",0.9,False,"click",None)]),
    ("droppedP",0.7,False,"click",None),
    ("closeoven",0.925,False,"confirmer",None),
    ("closeoven",0.925,False,"click",None),
    ("openoven",0.925,True,"left",None),
    ("back",0.75,False,"right",None),
    ("openoven",0.85,False,"click",None),
    ("openoven",0.925,True,"confirmer",None),
    ("openoven",0.925,True,"left",None),
    ("closeoven",0.925,False,"click",None),
    ("wrench",0.95,False,"click",None),

    # === PICK YELLOW ===
    ("wrenched",0.9,False,"click",y),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),

    # === DROP YELLOW ===
    ("info",0.9,False,"confirmer",None),
    ("yellowchem",0.9,False,"click",None),
    ("pickedY",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP BLUE ===
    ("info",0.9,False,"confirmer",None),
    ("bluechem",0.9,False,"click",None),
    ("pickedB",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP PINK ===
    ("info",0.9,False,"confirmer",None),
    ("pinkchem",0.9,False,"click",None),
    ("pickedP",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # === COMBINE M === #
    ("info",0.9,False,"confirmer",None),
    ("punched",0.9,True,"if",[("punch",0.9,False,"click",None)]),
    ("droppedP",0.7,False,"click",None),
    ("closeoven",0.925,False,"confirmer",None),
    ("closeoven",0.925,False,"click",None),
    ("openoven",0.925,True,"left",None),
    ("back",0.75,False,"right",None),
    ("openoven",0.85,False,"click",None),
    ("openoven",0.925,True,"confirmer",None),
    ("openoven",0.925,True,"left",None),
    ("closeoven",0.925,False,"click",None),
    ("wrench",0.95,False,"click",None),

    # === PICK YELLOW ===
    ("wrenched",0.9,False,"click",y),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),
    # # === PICK BLUE ===
    ("info",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",b),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),

    # === DROP YELLOW ===
    ("info",0.9,False,"confirmer",None),
    ("yellowchem",0.9,False,"click",None),
    ("pickedY",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),
    
    # # === DROP BLUE ===
    ("info",0.9,False,"confirmer",None),
    ("bluechem",0.9,False,"click",None),
    ("pickedB",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP PINK ===
    ("info",0.9,False,"confirmer",None),
    ("pinkchem",0.9,False,"click",None),
    ("pickedP",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # === COMBINE M === # 
    ("info",0.9,False,"confirmer",None),
    ("punched",0.9,True,"if",[("punch",0.9,False,"click",None)]),
    ("droppedP",0.7,False,"click",None),
    ("closeoven",0.925,False,"confirmer",None),
    ("closeoven",0.925,False,"click",None),
    ("openoven",0.925,True,"left",None),
    ("back",0.75,False,"right",None),
    ("openoven",0.85,False,"click",None),
    ("openoven",0.925,True,"confirmer",None),
    ("openoven",0.925,True,"left",None),
    ("closeoven",0.925,False,"click",None),
    ("wrench",0.95,False,"click",None),

    # === PICK YELLOW ===
    ("wrenched",0.9,False,"click",y),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),

    # === DROP YELLOW ===
    ("info",0.9,False,"confirmer",None),
    ("yellowchem",0.9,False,"click",None),
    ("pickedY",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP BLUE ===
    ("info",0.9,False,"confirmer",None),
    ("bluechem",0.9,False,"click",None),
    ("pickedB",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP PINK ===
    ("info",0.9,False,"confirmer",None),
    ("pinkchem",0.9,False,"click",None),
    ("pickedP",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # === COMBINE M === # 
    ("info",0.9,False,"confirmer",None),
    ("punched",0.9,True,"if",[("punch",0.9,False,"click",None)]),
    ("droppedP",0.7,False,"click",None),
    ("closeoven",0.925,False,"confirmer",None),
    ("closeoven",0.925,False,"click",None),
    ("openoven",0.925,True,"left",None),
    ("back",0.75,False,"right",None),
    ("openoven",0.85,False,"click",None),
    ("openoven",0.925,True,"confirmer",None),
    ("openoven",0.925,True,"left",None),
    ("closeoven",0.925,False,"click",None),


    # === MAKE FUEL 

    # === PICK BLUE ===
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",b),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),
    
    # === DROP GREEN ===
    ("info",0.9,False,"confirmer",None),
    ("greenchem",0.9,False,"click",None),
    ("pickedG",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP BLUE ===
    ("info",0.9,False,"confirmer",None),
    ("bluechem",0.9,False,"click",None),
    ("pickedB",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP MYST ===
    ("info",0.9,False,"confirmer",None),
    ("mystchem",0.9,False,"click",None),
    ("pickedM",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None), 
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]), 

    # === COMBINE FUEL ===
    ("info",0.9,False,"confirmer",None),
    ("punched",0.9,True,"if",[("punch",0.9,False,"click",None)]),
    ("droppedM",0.8,False,"click",None),
    ("closeoven",0.925,False,"confirmer",None),
    ("closeoven",0.925,False,"click",None),
    ("openoven",0.925,True,"left",None),
    ("back",0.75,False,"right",None),
    ("openoven",0.85,False,"click",None),
    ("openoven",0.925,True,"confirmer",None),
    ("openoven",0.925,True,"left",None),
    ("closeoven",0.925,False,"click",None),


    # # === PICK GREEN ===
    ("info",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",g),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),

    # === DROP GREEN ===
    ("info",0.9,False,"confirmer",None),
    ("greenchem",0.9,False,"click",None),
    ("pickedG",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP BLUE ===
    ("info",0.9,False,"confirmer",None),
    ("bluechem",0.9,False,"click",None),
    ("pickedB",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP MYST ===
    ("info",0.9,False,"confirmer",None),
    ("mystchem",0.9,False,"click",None),
    ("pickedM",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),  
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # === COMBINE FUEL ===
    ("info",0.9,False,"confirmer",None),
    ("punched",0.9,True,"if",[("punch",0.9,False,"click",None)]),
    ("droppedM",0.8,False,"click",None),
    ("closeoven",0.925,False,"confirmer",None),
    ("closeoven",0.925,False,"click",None),
    ("openoven",0.925,True,"left",None),
    ("back",0.75,False,"right",None),
    ("openoven",0.85,False,"click",None),
    ("openoven",0.925,True,"confirmer",None),
    ("openoven",0.925,True,"left",None),
    ("closeoven",0.925,False,"click",None),
    

    # # === MAKE SLIME ===

    ("wrench",0.95,False,"click",None),
    # === PICK GREEN ====
    ("info",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",g),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),

    # # === PICK PINK ===
    ("info",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",p),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),
    # # === PICK BLUE ===

    # === DROP GREEN ===
    ("info",0.9,False,"confirmer",None),
    ("greenchem",0.9,False,"click",None),
    ("pickedG",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP BLUE ===
    ("info",0.9,False,"confirmer",None),
    ("bluechem",0.9,False,"click",None),
    ("pickedB",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP P ===
    ("info",0.9,False,"confirmer",None),
    ("pinkchem",0.9,False,"click",None),
    ("pickedP",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),  
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # === COMBINE SLIME ===
    ("info",0.9,False,"confirmer",None),
    ("punched",0.9,True,"if",[("punch",0.9,False,"click",None)]),
    ("droppedP",0.7,False,"click",None),
    ("closeoven",0.925,False,"confirmer",None),
    ("closeoven",0.925,False,"click",None),
    ("openoven",0.925,True,"left",None),
    ("back",0.75,False,"right",None),
    ("openoven",0.85,False,"click",None),
    ("openoven",0.925,True,"confirmer",None),
    ("openoven",0.925,True,"left",None),
    ("closeoven",0.925,False,"click",None),

    # # === PICK PINK ===
    ("info",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",p),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),
    # # === PICK BLUE ===
    ("info",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",b),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),
    # === PICK GREEN ====
    ("info",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",g),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),

    # === DROP GREEN ===
    ("info",0.9,False,"confirmer",None),
    ("greenchem",0.9,False,"click",None),
    ("pickedG",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP BLUE ===
    ("info",0.9,False,"confirmer",None),
    ("bluechem",0.9,False,"click",None),
    ("pickedB",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP P ===
    ("info",0.9,False,"confirmer",None),
    ("pinkchem",0.9,False,"click",None),
    ("pickedP",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None), 
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]), 

    # === COMBINE SLIME ===
    ("info",0.9,False,"confirmer",None),
    ("punched",0.9,True,"if",[("punch",0.9,False,"click",None)]),
    ("droppedP",0.7,False,"click",None),
    ("closeoven",0.925,False,"confirmer",None),
    ("closeoven",0.925,False,"click",None),
    ("openoven",0.925,True,"left",None),
    ("back",0.75,False,"right",None),
    ("openoven",0.85,False,"click",None),
    ("openoven",0.925,True,"confirmer",None),
    ("openoven",0.925,True,"left",None),
    ("closeoven",0.925,False,"click",None),

    # === PICK GREEN ====
    ("info",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",g),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),

    # === DROP GREEN ===
    ("info",0.9,False,"confirmer",None),
    ("greenchem",0.9,False,"click",None),
    ("pickedG",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP BLUE ===
    ("info",0.9,False,"confirmer",None),
    ("bluechem",0.9,False,"click",None),
    ("pickedB",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP P ===
    ("info",0.9,False,"confirmer",None),
    ("pinkchem",0.9,False,"click",None),
    ("pickedP",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),  
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # === COMBINE SLIME ===
    ("info",0.9,False,"confirmer",None),
    ("punched",0.9,True,"if",[("punch",0.9,False,"click",None)]),
    ("droppedP",0.7,False,"click",None),
    ("closeoven",0.925,False,"confirmer",None),
    ("closeoven",0.925,False,"click",None),
    ("openoven",0.925,True,"left",None),
    ("back",0.75,False,"right",None),
    ("openoven",0.85,False,"click",None),
    ("openoven",0.925,True,"confirmer",None),
    ("openoven",0.925,True,"left",None),
    ("closeoven",0.925,False,"click",None),

    # === PICK GREEN ====
    ("info",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",g),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),

    # === DROP GREEN ===
    ("info",0.9,False,"confirmer",None),
    ("greenchem",0.9,False,"click",None),
    ("pickedG",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP BLUE ===
    ("info",0.9,False,"confirmer",None),
    ("bluechem",0.9,False,"click",None),
    ("pickedB",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP P ===
    ("info",0.9,False,"confirmer",None),
    ("pinkchem",0.9,False,"click",None),
    ("pickedP",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),  
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # === COMBINE SLIME ===
    ("info",0.9,False,"confirmer",None),
    ("punched",0.9,True,"if",[("punch",0.9,False,"click",None)]),
    ("droppedP",0.7,False,"click",None),
    ("closeoven",0.925,False,"confirmer",None),
    ("closeoven",0.925,False,"click",None),
    ("openoven",0.925,True,"left",None),
    ("back",0.75,False,"right",None),

    # === IF SLIME MAX ===
    ("slime200",0.9,False,"if",[
        ("wrench",0.95,False,"click",None),
        ("wrenched",0.9,False,"confirmer",None),
        ("StorageW",0.9,False,"click",None),
        ("deposit",0.9,False,"click",None),
        ("info",0.9,False,"confirmer",None),
        ("slime",0.9,False,"click",None),
        ("storeitems",0.9,False,"click",None),
        ("x",0.9,False,"click",None),
        ("openoven",0.925,True,"left",None),
        ("back",0.75,False,"right",None) ]),

    ("openoven",0.85,False,"click",None),
    ("openoven",0.925,True,"confirmer",None),
    ("openoven",0.925,True,"left",None),
    ("closeoven",0.925,False,"click",None),


    # === MAKE SHOCKINATOR

    # === PICK GREEN ===
    ("wrench",0.95,False,"click",None),
    ("wrenched",0.9,False,"click",g),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),

    # === DROP GREEN ===
    ("info",0.9,False,"confirmer",None),
    ("greenchem",0.9,False,"click",None),
    ("pickedG",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP RED ===
    ("info",0.9,False,"confirmer",None),
    ("redchem",0.9,False,"click",None),
    ("pickedR",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP PINK ===
    ("info",0.9,False,"confirmer",None),
    ("pinkchem",0.9,False,"click",None),
    ("pickedP",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),  
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),


    # === COMBINE SHOCKINATOR ===
    ("info",0.9,False,"confirmer",None),
    ("punched",0.9,True,"if",[("punch",0.9,False,"click",None)]),
    ("droppedP",0.7,False,"click",None),
    ("closeoven",0.925,False,"confirmer",None),
    ("closeoven",0.925,False,"click",None),
    ("openoven",0.925,True,"left",None),
    ("back",0.75,False,"right",None),
    ("openoven",0.85,False,"click",None),
    ("openoven",0.925,True,"confirmer",None),
    ("openoven",0.925,True,"left",None),
    ("closeoven",0.925,False,"click",None),

    # === PICK GREEN ===
    ("wrench",0.95,False,"click",None),
    ("wrenched",0.9,False,"click",g),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),
    # # === PICK PINK ===
    ("info",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",p),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),

    # === DROP GREEN ===
    ("info",0.9,False,"confirmer",None),
    ("greenchem",0.9,False,"click",None),
    ("pickedG",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP RED ===
    ("info",0.9,False,"confirmer",None),
    ("redchem",0.9,False,"click",None),
    ("pickedR",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),

    # # === DROP PINK ===
    ("info",0.9,False,"confirmer",None),
    ("pinkchem",0.9,False,"click",None),
    ("pickedP",0.925,False,"confirmer",None),
    ("drop",0.9,False,"click",None),
    ("ok",0.9,False,"click",None),  
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),


    # === COMBINE SHOCKINATOR ===
    ("info",0.9,False,"confirmer",None),
    ("punched",0.9,True,"if",[("punch",0.9,False,"click",None)]),
    ("droppedP",0.7,False,"click",None),
    ("closeoven",0.925,False,"confirmer",None),
    ("closeoven",0.925,False,"click",None),
    ("openoven",0.925,True,"left",None),
    ("back",0.75,False,"right",None),

    # === STORAGE ===

    ("wrench",0.95,False,"click",None),
    ("wrenched",0.9,False,"confirmer",None),
    ("StorageW",0.9,False,"click",None),
    ("deposit",0.9,False,"click",None),
    ("info",0.9,False,"confirmer",None),
    ("slime",0.9,False,"click",None),
    ("storeitems",0.9,False,"click",None),
    ("deposit",0.9,False,"click",None),
    ("info",0.9,False,"confirmer",None),
    ("shockinator",0.9,False,"click",None),
    ("storeitems",0.9,False,"click",None),
    ("x",0.9,False,"click",None),


    # # === RECYCLE RED ===

    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",r),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),
    ("info",0.9,False,"confirmer",None),
    ("redchem",0.9,False,"click",None),
    ("pickedR",0.925,False,"confirmer",None),
    ("recycle",0.9,False,"click",None),
    ("ok",0.9,False,"write","200"),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),
    ("info",0.9,False,"confirmer",None),


    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",r),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),
    ("info",0.9,False,"confirmer",None),
    ("redchem",0.9,False,"click",None),
    ("pickedR",0.925,False,"confirmer",None),
    ("recycle",0.9,False,"click",None),
    ("ok",0.9,False,"write","200"),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),
    ("info",0.9,False,"confirmer",None),

    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",r),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),
    ("info",0.9,False,"confirmer",None),
    ("redchem",0.9,False,"click",None),
    ("pickedR",0.925,False,"confirmer",None),
    ("recycle",0.9,False,"click",None),
    ("ok",0.9,False,"write","200"),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),
    ("info",0.9,False,"confirmer",None),

    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",r),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),
    ("info",0.9,False,"confirmer",None),
    ("redchem",0.9,False,"click",None),
    ("pickedR",0.925,False,"confirmer",None),
    ("recycle",0.9,False,"click",None),
    ("ok",0.9,False,"write","200"),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),
    ("info",0.9,False,"confirmer",None),

    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",r),
    ("RetItems",0.9,False,"click",None),
    ("Retrieve",0.9,False,"click",None),
    ("info",0.9,False,"confirmer",None),
    ("redchem",0.9,False,"click",None),
    ("pickedR",0.925,False,"confirmer",None),
    ("recycle",0.9,False,"click",None),
    ("ok",0.9,False,"write","200"),
    ("ok",0.9,False,"click",None),
    ("ok",0.9,True,"confirmer",None),
    ("info",0.9,True,"if",[("scroll",0.8,False,"click",None)]),
    ("info",0.9,False,"confirmer",None),

    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"click",r),
    ("close",0.9,False,"confirmer",None),
    ("change",0.9,False,"if",[("close",0.9,False,"click",None)]),
    ("change",0.9,True,"if",[("RetItems",0.9,False,"click",None),
                            ("Retrieve",0.9,False,"click",None),
                            ("info",0.9,False,"confirmer",None),
                            ("200chemR",0.9,False,"if",[
                                ("redchem",0.9,False,"click",None),
                                ("pickedR",0.925,False,"confirmer",None),
                                ("recycle",0.9,False,"click",None),
                                ("ok",0.9,False,"write","200"),
                                ("ok",0.9,False,"click",None),
                                ("ok",0.9,True,"confirmer",None),]),
                            ("info",0.9,True,"if",[
                                ("scroll",0.8,False,"click",None)]) ]),
    
    

    # === RESTOCK ===
    ("info",0.9,False,"confirmer",None),
    ("punched",0.9,True,"if",[("punch",0.9,False,"click",None)]),
    ("self",0.9,False,"click",None),
    ("entering",0.9,False,"confirmer",None),
    ("clock",0.9,False,"confirmer",None),
    ("wrenched",0.9,True,"if",[("wrench",0.95,False,"click",None)]),
    ("wrenched",0.9,False,"right",1),
    ("self",0.9,False,"click",None),
    ("insfuel",0.9,False,"click",None),
    ("digivend",0.9,False,"breaker",None),
    ("addthem",0.9,False,"click",None),
    ("machine",0.9,False,"confirmer",None),
    ("punched",0.9,True,"if",[("punch",0.9,False,"click",None)]),
    ("punched",0.9,False,"confirmer",None),
    ("menu",0.9,False,"click",None),
    ("exit",0.9,False,"click",None),
    ("wrld",0.9,False,"click",None),
    ("wrld",0.9,False,"backspace",None),
    ("wrld",0.9,True,"write","world"),
    ("enterworld",0.9,False,"click",None),
    ("enterworld",0.9,True,"breaker",None),
    ("hiddendoor",0.9,False,"right",0.25),
    ("entering",0.9,False,"breaker",None),
    ("entering",0.9,False,"confirmer",None),
]

