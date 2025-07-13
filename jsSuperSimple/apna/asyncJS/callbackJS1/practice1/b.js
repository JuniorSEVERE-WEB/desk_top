let stocks = {
    Fuits: ["strawberry", "grapes", "banana", "apple"],
    liquid: ["water", "ice"],
    holder: ["cone", "cup", "stick"],
    toppings: ["chocolate", "peanuts"],
};

let order = (Fruit_name, call_production)=>{
    setTimeout(()=>{
        console.log(`${stocks.Fuits[Fruit_name]} was selected`);
        call_production();
        
    },2000)
};

let production = ()=>{
   setTimeout(()=>{
     console.log('productiion has started');
   },0)
    
};

order(0,production);