var alreadyPlaying = false;
var audioRange = 0.8;
var currentAudioStatus = 0;

var PlyCRT = null;
var TMPPlyBTN = null;


var Dispid = null;
var loopDisp = null;
var audioPlayedstatus = 0;
 for(var i = 0 ; document.getElementById(i); i++){
        	i++;
        }
var allMediaTracks = i-1;

if(!document.getElementsByClassName("audioFile")){
	document.getElementById("footer").classList.add("fixed-bottom");
}else{
	if(!document.getElementById("footer").classList.contains("fixed-bottom")){
		document.getElementById("footer").classList.remove("fixed-bottom");
	}
}

function PlyPRVAudio(){
	prevNextDisable(PlyCRT.id);
	var plyprv = PlyCRT.id;
	plyprv--;
	PlyCRTAudio(plyprv);
}
function PlyCRTAudio(file){
	Dispid = file;
	var filetoplay = document.getElementById(file);
	statusAudioRange(file, audioRange);
	playPausebtn = 'playPause'+file;
	if(alreadyPlaying && filetoplay === PlyCRT){
		filetoplay.pause();
		changePlayingStat(playPausebtn);
		if(loopDisp){
			clearInterval(loopDisp);
		}
		return alreadyPlaying = false;
	}
	if(alreadyPlaying){
		PlyCRT.pause();
		prevNextDisable(PlyCRT.id);
		changePlayingStat(TMPPlyBTN);
		filetoplay.play();
		changePlayingStat(playPausebtn);
		loopDisp = window.setInterval(playSeriesStatus, 1000);
	}else{
		filetoplay.play();
		alreadyPlaying = true;
		changePlayingStat(playPausebtn);
		loopDisp = window.setInterval(playSeriesStatus, 1000);
	}
	PlyCRT = filetoplay;
	prevNextStatus(file, allMediaTracks);
	TMPPlyBTN = playPausebtn;
}

function PlyNXTAudio(){
	prevNextDisable(PlyCRT.id);
	var plynxt = PlyCRT.id;
	plynxt++;
	PlyCRTAudio(plynxt);
}



function statusAudio(path, file){
	var filetoplay = document.getElementById(file);
	var lengthOfAudio = filetoplay.duration;
	var currentTimeOfAudio = filetoplay.currentTime;
	var playedAudio = filetoplay.played;
}
function statusAudioRange(id, val){
	var filetoply = document.getElementById(id)
	filetoply.volume = val;
	document.getElementById('audioLevel'+id).value = val*10;
}

function MoveOrDeleteTheFile(file , id, actionOnFile){
	action = 'actionOnFile'+id;
	Mediafile = 'FileToApply'+id;
	document.getElementById(action).value = actionOnFile;
	document.getElementById(Mediafile).value = file;
}



function changePlayingStat(id){
	curentaudiostatus = document.getElementById(id).innerHTML;
	if(curentaudiostatus == '▶'){
		document.getElementById(id).innerHTML = '⏸';
	}else{
		document.getElementById(id).innerHTML = '▶';
	}
}

function playSeriesStatus(){
	if (Dispid){
		AudioStatus = 'AudioStatus' + Dispid;
		var duration = document.getElementById(Dispid).duration;			//198/60			min 3 		sec 18
		var currentTime = document.getElementById(Dispid).currentTime;	//30
		audioPlayedstatus  = currentTime
		audioPlayedstatus += 1;
		var minPassed = Math.floor(currentTime/60);
		var secPassed = Math.floor(currentTime%60);
		var minAll = Math.floor(duration/60);
		var secAll = Math.floor(duration%60);
		var text_status_disp =  minPassed + ':' + secPassed + ' 🕧 ' + minAll + ':' + secAll;
		


		// var text_status_disp =  currentTime/60 + ':' + duration/60;
		document.getElementById('text_status' + Dispid).innerHTML = text_status_disp;
		document.getElementById(AudioStatus).setAttribute("max", duration)
		document.getElementById(AudioStatus).value = audioPlayedstatus;
	}else{
		clearInterval(loopDisp);
	}
}
function prevNextDisable(file){
        document.getElementById('prev'+file).setAttribute("disabled", "");
        document.getElementById('next'+file).setAttribute("disabled", "");
}
function prevNextStatus(file, allfiles){
	if(PlyCRT.id == file){
		if(document.getElementById('prev'+file).hasAttribute('disabled') || document.getElementById('next'+file).hasAttribute('disabled')){
			if(file == 0){
				if(allfiles == 1 && allfiles != 0){
			        document.getElementById('prev'+file).setAttribute("disabled", "");
			        document.getElementById('next'+file).setAttribute("disabled", "");
				}else{
			        document.getElementById('prev'+file).setAttribute("disabled", "");
			        document.getElementById('next'+file).attributes.removeNamedItem("disabled");
				}
			}else{
				if(file != allfiles-1){
			        document.getElementById('prev'+file).attributes.removeNamedItem("disabled");
			        document.getElementById('next'+file).attributes.removeNamedItem("disabled");
				}else{
			        document.getElementById('prev'+file).attributes.removeNamedItem("disabled");
			        document.getElementById('next'+file).setAttribute("disabled", "");
			    }
			}
		}
	}else{
		if(file == 0 && allfiles == 1){
	        document.getElementById('prev'+file).setAttribute("disabled", "");
	        document.getElementById('next'+file).setAttribute("disabled", "");
		}else if(file == 0 && allfiles > 1){
	        document.getElementById('prev'+file).setAttribute("disabled", "");
	        document.getElementById('next'+file).attributes.removeNamedItem("disabled");
		}else if(file != 0 && file == allfiles-1){
	        document.getElementById('prev'+file).attributes.removeNamedItem("disabled");
	        document.getElementById('next'+file).setAttribute("disabled", "");
		}else if(file != 0 && file != allfiles-1){
	        document.getElementById('prev'+file).attributes.removeNamedItem("disabled");
	        document.getElementById('next'+file).attributes.removeNamedItem("disabled");
		}
	}
}

function manualChange(file){
	var value = document.getElementById('AudioStatus'+file).value;
	document.getElementById(file).currentTime = value;
}
function audioChange(id){
	audioRange = document.getElementById('audioLevel'+id).value/10;
	statusAudioRange(id, audioRange);
}