// let result = srv.split(',')
// console.log('result--->',result);


// let number;

// for(let i=0;i<5;i++){
//     number =  i

//     setTimeout(()=>{
//         console.log("number", i);

//     },1000)
// }
//c++


function get_month_end_date(date) {
    date = new Date(date);
    return new Date(date.getFullYear(), date.getMonth() + 1, 0);
}
/**  use for calculating credit suggestion based on start_date and till_date, support multiple month */
function calculateCreditSuggestionLimit(startDate, tillDate, totalSales) {
    console.log("====================================================");
    console.log("start_date-->", startDate.toLocaleDateString('fr-CA'),
     "till_date-->", tillDate.toLocaleDateString('fr-CA'));

    const totalDays = Math.abs((tillDate - startDate) / (1000 * 60 * 60 * 24)) + 1;

    const monthEnd = new Date(startDate.getFullYear(), startDate.getMonth() + 1, 0);

    console.log("total_days-->", totalDays, "month_end-->", monthEnd.getDate());

    if (tillDate > monthEnd) {
        const calculateDay = Math.abs((monthEnd - startDate) / (1000 * 60 * 60 * 24)) + 1;
        console.log("calculate_day-->", calculateDay);
        const amount = (totalSales / monthEnd.getDate()) * calculateDay;
        console.log("bill amount-->", amount);

        startDate = new Date(monthEnd.getFullYear(), monthEnd.getMonth(), monthEnd.getDate() + 1);

        return amount + calculateCreditSuggestionLimit(startDate, tillDate, totalSales);
    } else {
        const amount = (totalSales / monthEnd.getDate()) * totalDays;
        console.log("bill amount-->", amount);
        return amount;
    }
}

const salesAmount = 502;
const billingScheme = 65;
const today = new Date();
const startDate = new Date(today.getFullYear(), today.getMonth(), 1);
const tillDate = new Date(startDate.getFullYear(), startDate.getMonth(), startDate.getDate() + billingScheme - 1);


// console.log(Math.round(calculateTotalLimit(startDate, tillDate, salesAmount)));

// function data_gen(a,call_back){
//     setTimeout(() => {
//         a = 5
//         call_back(a)
        
//     }, 2000);
// }

// console.log('print a');
// console.log('print b');
// var a = 1

// data_gen(a,(data)=>{
//     let sum  =  15 + data
//     console.log('sum-->',sum);
//     console.log('print c');
// })




// 1. callback 2.promise 3. async/await


// result.then((value)=>{
//     let sum  =  15 + value
//     console.log('sum-->',sum);
//     console.log('print c');
// },err=>{
//     console.log('print reject',err);
// })

var  fetchw = {
    other_property : 'something',
    a : 1,
    b : 1,
    post : function(url){
        
        return new Promise ((resolve,reject)=> {
            setTimeout(() => {
                if(this.a==this.b){
                    console.log("I am waiting for 2 minutes")
                    resolve(100)
                }else{
                    reject("a is not equal to b")
                }
            }, 2000);
        })
    } 
}


async function main(){

    console.log('print a');
    console.log('print b');
    

    // let fetch =  new Promise((resolve,reject)=>{
    //     setTimeout(() => {
    //         if(a==b){
    //             console.log("I am waiting for 2 minutes")
    //             resolve(100)
    //         }else{
    //             reject("a is not equal to b")
    //         }
    //     }, 2000);
    // })
    
    let result =  await fetch('https://dummyjson.com/products/1',{
        method  : 'GET',
    }).json()
    console.log("result-->", result);

    // let value = await fetchw.post('url').catch(err=>{
    //     console.log(err);
    // });
    // console.log("sum-->", value + 10);
    // console.log("something else=-->");
}

// main()



// synchronies - 
// asynchronies - 


let billing = [
    {start_date : '2024-02-01',particular: 'IIG', bw : 10,sales_price : 100},
    {start_date : '2024-02-10',particular: 'IIG', bw : 10,sales_price : 100},
    {start_date : '2024-02-01',particular: 'GGC', bw : 10,sales_price : 100},
    {start_date : '2024-02-15',particular: 'GGC', bw : 10,sales_price : 100},
    {start_date : '2024-02-10',particular: 'GGC', bw : 10,sales_price : 100},
    {start_date : '2024-02-01',particular: 'IPT', bw : 10,sales_price : 100},
    {start_date : '2024-02-10',particular: 'IPT', bw : 10,sales_price : 100},
    {start_date : '2024-02-15',particular: 'IPT', bw : 10,sales_price : 100},
    {start_date : '2024-02-25',particular: 'CDN', bw : 10,sales_price : 100},
]

//group By

// var result =  billing.reduce((prev,curr)=>{
//     (prev[curr.start_date] = prev[curr.start_date] || []).push(curr)
//     return prev
// },{})
// console.log("result-->", result);
