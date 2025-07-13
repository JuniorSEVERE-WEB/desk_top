let order = (call_production)=>{
    console.log("order placed, please call production");
    call_production();
}


let production = ()=>{
    console.log("order receive, starting productionz");
    
}
order(production);



/*let order = (call_production)=> {
    console.log("order placed, please call production");
    call_production()
};

let production = ()=>{
    console.log("order receive, starting production")
};

order(production);
*/