var http = require('http');
var formidable = require('formidable');
var fs = require('fs');

var db = require('mongojs').connect('mongodb://bstill:unique@ds043991.mongolab.com:43991/uniq_snowflake');
var courses = db.collection('courses');


//Create and write data to sample web page on locally hosted server 
http.createServer(function(req,res){
	if (req.method.toLowerCase() == 'post'){
		var form = new formidable.IncomingForm();
		form.parse(req, function(err, fields, files){
			var key = Object.keys(fields);
			courses.find({"Course": key[0]}, function(err, data){
				if (err) {
					console.log("Error: " + err);	
				}
				res.writeHeader(200, {"Content-Type": "text/plain", 'Access-Control-Allow-Origin': '*'});  
				res.write(JSON.stringify(data), null, ' ');  
				res.end();
			});
      	});
	}
}).listen(8080);
console.log("Server running on 8080"); 

