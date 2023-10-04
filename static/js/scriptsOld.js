console.log(" page is ready for use");

var filelist = new Array();

updateList = function () {
    var input = document.getElementById('fileUploader');
    var output = document.getElementById('divFiles');

    var HTML = "";
   // var path = "file:///H:/Music/---/111/"
    var path = input.value;
    
    for (var i = 0; i < 4; ++i) {
        //filelist[i] = input.files.item(i).name;
        filelist.push(path.item(i).name);
        
        console.log(input.files.item(i).webkitRelativePath)
        if(i == 0){
          HTML = `
          <audio width="500" height="300" controls >         
              <source src="${path}${filelist[i]}" >
          </audio>
          `
        }else{   
          HTML += `
          <audio width="500" height="300" controls >         
              <source src="${path}${filelist[i]}" >
          </audio>
          `
        }
        
    }
    output.innerHTML = HTML;
}




function showAvailableDrives()
{
  document.write(getDriveList());
}

function getDriveList()
{
  var fso, s, n, e, x;
  fso = new ActiveXObject('scripting.FilesystemObject');
  e = new Enumerator(fso.Drives);
  s = '';
  do {
    x = e.item();
    s = s + x.DriveLetter;
    s += ':- ';
    if(x.DriveType == 3)n = x.ShareName;
    else if(x.IsReady)n = x.VolumeName;
    else n = '[Drive not ready]';
    s += n + '<br>';
    e.moveNext();
  }
  while (!e.atEnd());
  return (s);
  
}




// var filelist = new Array();

// updateList = function () {
//     var input = document.getElementById('fileUploader');
//     var output = document.getElementById('divFiles');

//     var HTML = "<table>";
//     for (var i = 0; i < input.files.length; ++i) {
//         //filelist[i] = input.files.item(i).name;
//         filelist.push(input.files.item(i).name);
//         HTML += "<tr><td>" 
//               + filelist[i] 
//               + "</td><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<button ></button></td></tr>";
//     }
//     HTML += "</table>";
//     output.innerHTML = HTML;
//     console.log(filelist);
// }



// how to find the source of a file
//   var x = document.getElementById("myImg").src;
//   document.getElementById("demo").innerHTML = x;




// yFunction() {
//     var x = document.getElementById("frm1");
//     var text = "";
//     var i;
//     for (i = 0; i < x.length ;i++) {
//       text += x.elements[i].value + "<br>";
//     }
//     document.getElementById("demo").innerHTML = text;
//   }




//   var x = document.createElement("INPUT");
// x.setAttribute("type", "file");




// file:///K:/Websites/w3%20school/www.w3schools.com/tags/ref_av_dom.html
