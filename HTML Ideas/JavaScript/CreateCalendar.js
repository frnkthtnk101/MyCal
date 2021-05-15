var TheMonths = ["January", "Feburary", "March", "April","May", "June", "July", "August", "September", "October", "November", "Decemeber"];
var TodaysDate = new Date();

var ThisMonth = TodaysDate.getMonth();
var  firstOfTheMonth = new Date(TodaysDate.getFullYear(),ThisMonth,1);
var UtcDay = firstOfTheMonth.getDay();

//Make the month tag correct
var monthPlaceHolder = document.getElementById("MonthName");
monthPlaceHolder.innerText = TheMonths[ThisMonth] + ' ' + firstOfTheMonth.getFullYear();

//var DaysInCalendar = new Array(UtcDay).fill(0);
var CurrentMonth = ThisMonth;
var DaysInCalendar = new Array();
while(UtcDay > 0)
{
    var pastDate = new Date(firstOfTheMonth.getTime());
    pastDate.setDate(pastDate.getDate() - UtcDay);
    DaysInCalendar.push(pastDate.getDate());
    UtcDay -=1
} 
/*  
do{
    DaysInCalendar.push(firstOfTheMonth.getDate());
    firstOfTheMonth.setDate(firstOfTheMonth.getDate() + 1);
    CurrentMonth =  firstOfTheMonth.getMonth();
}while(CurrentMonth == ThisMonth);
while(firstOfTheMonth.getDay() < 6){
    DaysInCalendar.push(firstOfTheMonth.getDate());
    firstOfTheMonth.setDate(firstOfTheMonth.getDate() + 1);
}*/
var index = 0;
var lenghtOfArray = DaysInCalendar.length;
var calendar = document.getElementById("CalTable");
for(i = 0; i < 6; i+=1){
    var row = calendar.insertRow(i+1);
    for(j = 0; j < 7; j +=1 )
    {
        var cell = row.insertCell(j);
        if(index < lenghtOfArray)
        {
            cell.innerText = DaysInCalendar[index] == 0? "" : DaysInCalendar[index];
            index +=1;
        }
        else
        {
            cell.innerText = firstOfTheMonth.getDate();
            firstOfTheMonth.setDate(firstOfTheMonth.getDate() + 1);
        }
    }
}
