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

let production = ()=> {
    setTimeout(()=>{
       console.log("production has started");
       
    },0000)
};
order(0,production);

/*
TIME(SECONDS)
#1 Place order -> 2
#2 Cut the fruit ->2
#3 Add water and ice ->1
#4 start the machine ->1
#5 select toppings ->3
#7 serve ice cream ->2

*/

