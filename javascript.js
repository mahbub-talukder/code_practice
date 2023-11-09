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

        return amount + calculateTotalLimit(startDate, tillDate, totalSales);
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


console.log(Math.round(calculateTotalLimit(startDate, tillDate, salesAmount)));