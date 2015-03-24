//Import auxiliary libraries
var mongoose = require('mongoose');
var http = require('http');
var Schema = mongoose.Schema;


var to_print;

//Connect to the MongoDB 'course_catalog'
mongoose.connect('mongodb://bstill:unique@ds043991.mongolab.com:43991/uniq_snowflake');
mongoose.connection.on("open", function(){
  console.log("mongodb is connected!!");
});


//Accessing the data in the 'courses' collection in 'course_catalog' MongoDB
data_set = new mongoose.Schema({}, {collection: 'courses'});
var catalog = mongoose.model('catalog', data_set);
catalog.find({'Instructor_ln': 'Kaplan'}, 'Title Course', function(err, data) { 
	//console.log(data);
	to_print = data; 
})


//Create and write data to sample web page on locally hosted server 
http.createServer(function(req,res){  
    res.writeHeader(200, {"Content-Type": "text/plain"});  
    res.write(String(to_print));  
    res.end();  
}).listen(8080);
console.log("Server Running on 8080");  
