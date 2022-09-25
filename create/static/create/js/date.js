function set2fig(num) {
  // 桁数が1桁だったら先頭に0を加えて2桁に調整する
  var ret;
  if( num < 10 ) { ret = "0" + num; }
  else { ret = num; }
  return ret;
}
function Time() {
  var dt = new Date();
  var month = dt.getMonth()+1;
  var date = dt.getDate();
  var year = dt.getFullYear();
  dateT = ["SUN DAY","MON DAY","TUES DAY","WEDNES DAY","THURS DAY","FRI DAY","SATUR DAY"];
  var day = dateT[dt.getDay()];
  document.getElementById("year").innerHTML = year;
  document.getElementById("month").innerHTML = month;
  document.getElementById("date").innerHTML = date;
  document.getElementById("day").innerHTML = day;
}
setInterval('Time()',1);