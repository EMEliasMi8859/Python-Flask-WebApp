from flask import Flask, render_template, url_for, request, redirect
import os
import shutil

OrganizerApp = Flask(__name__)
###Audios
fileToDelete = 0
path_to_file = ""
tmpPath = ""
###Videos
Video_fileToDelete = 0
video_path_to_file = ""
video_tmpPath = ""



@OrganizerApp.route('/', methods=['GET', 'POST'])
def Main_Route():
    if(request.method == 'POST'):
        pass
    else:
        return render_template('index.html');
@OrganizerApp.route('/Audio', methods=['GET', 'POST'])
def Audio_Route():
    global path_to_file
    global tmpPath
    if(request.method == 'POST'):
        folder_path = request.form.get('path')
        folder_path = os.getcwd() + "\static\\" + folder_path
        try:
            obj = os.scandir(folder_path)
            all_files = []
            ids = 0
            name = []
            characters = int(len(str(folder_path)))
            folderPath = str(folder_path) + '\\'
            for entry in obj:
                if entry.is_dir() or entry.is_file():
                    if entry.is_file:
                        name = [entry.name, str(ids)]
                        all_files.append(name)
                        ids+=1
            path_to_file = folder_path[len(os.getcwd()):]+'\\'
            tmpPath = folder_path
            return render_template('Audio.html', files = all_files, path=path_to_file)
        except:
            if tmpPath != "":
                folder_path = tmpPath
            else:
                folder_path = os.getcwd() + "\static\AudiosToOrganize\\"
            obj = os.scandir(folder_path)
            all_files = []
            ids = 0
            name = []
            characters = int(len(str(folder_path)))
            folderPath = str(folder_path) + '\\'
            for entry in obj:
                if entry.is_dir() or entry.is_file():
                    if entry.is_file:
                        name = [entry.name, str(ids)]
                        all_files.append(name)
                        ids+=1

            path_to_file = folder_path[len(os.getcwd()):]+'\\'
            return render_template('Audio.html', files = all_files, path= path_to_file)

    elif(request.method == 'GET'):
        global fileToDelete


        os.chdir('static')
        directories = os.listdir()
        ToBeOrganize = True
        for dirs in directories:
            if (dirs == "AudiosToOrganize"):
                ToBeOrganize = False
        if ToBeOrganize:
            os.mkdir('AudiosToOrganize')
        os.chdir("../")

        if fileToDelete != 0:
            os.remove(fileToDelete)
            fileToDelete = 0
        if tmpPath != "":
            folder_path = tmpPath
        else:
            folder_path = os.getcwd() + "\static\AudiosToOrganize\\"
        obj = os.scandir(folder_path)
        all_files = []
        ids = 0
        name = []
        characters = int(len(str(folder_path)))
        folderPath = str(folder_path) + '\\'
        for entry in obj:
            if entry.is_dir() or entry.is_file():
                if entry.is_file:
                    name = [entry.name, str(ids)]
                    all_files.append(name)
                    ids+=1

        path_to_file = folder_path[len(os.getcwd()):]+'\\'
        return render_template('Audio.html', files = all_files, path= path_to_file)
@OrganizerApp.route('/ActionOnMedia', methods=['GET', 'POST'])
def ActionOnMedia_route():
    global path_to_file
    if(request.method  == 'POST'):
        cwd =  os.getcwd()
        os.chdir('static')
        directories = os.listdir()
        organized = True
        Fav = True
        Mix = True
        for dirs in directories:
            if (dirs == "Audios_Organized"):
                organized = False
        if organized:
            os.mkdir('Audios_Organized')
        os.chdir('Audios_Organized')
        directories = os.listdir()
        for dirs in directories:
            if dirs == "FAV":
                Fav = False
            elif dirs == "MIX":
                Mix = False
        if Fav:
            os.mkdir('FAV')
        if Mix:
            os.mkdir('MIX')
        os.chdir("../../")
        crtwrkdir = os.getcwd()
        actionToDo = request.form['actionOnFile'];
        fileToApply = request.form['FileToApply'];
        NewName = request.form['name']
        global fileToDelete
        if actionToDo == 'FAV':
            shutil.copy(crtwrkdir + path_to_file + fileToApply , crtwrkdir + '\static\Audios_Organized\FAV\\' + fileToApply)
            if NewName != "":
                os.rename(crtwrkdir + '\static\Audios_Organized\FAV\\' + fileToApply , crtwrkdir + '\static\Audios_Organized\FAV\\' + NewName + fileToApply[-4:])
            fileToDelete = crtwrkdir + path_to_file + fileToApply
            return redirect('/Audio')
        elif actionToDo == 'MIX':
            shutil.copy(crtwrkdir + path_to_file + fileToApply , crtwrkdir + '\static\Audios_Organized\MIX\\' + fileToApply)
            if NewName != "":
                os.rename(crtwrkdir + '\static\Audios_Organized\MIX\\' + fileToApply , crtwrkdir + '\static\Audios_Organized\MIX\\' + NewName + fileToApply[-4:])
            fileToDelete = crtwrkdir + path_to_file + fileToApply
            return redirect('/Audio')
        elif actionToDo == 'DEL':
            os.remove(crtwrkdir + path_to_file + fileToApply)
            return redirect('/Audio')









@OrganizerApp.route('/Video', methods=['GET', 'POST'])
def Video_Route():
    global video_path_to_file
    global video_tmpPath
    if(request.method == 'POST'):
        Video_folder_path = request.form.get('path')
        Video_folder_path = os.getcwd() + "\static\\" + Video_folder_path
        try:
            obj = os.scandir(Video_folder_path)
            all_files = []
            ids = 0
            name = []
            characters = int(len(str(Video_folder_path)))
            folderPath = str(Video_folder_path) + '\\'
            for entry in obj:
                if entry.is_dir() or entry.is_file():
                    if entry.is_file:
                        name = [entry.name, str(ids)]
                        all_files.append(name)
                        ids+=1
            video_path_to_file = Video_folder_path[len(os.getcwd()):]+'/'
            video_tmpPath = Video_folder_path
            return render_template('video.html', files = all_files, path=video_path_to_file)
        except:
            if video_tmpPath != "":
                Video_folder_path = video_tmpPath
            else:
                Video_folder_path = os.getcwd() + "\static\VideosToOrganize\\"
            obj = os.scandir(Video_folder_path)
            all_files = []
            ids = 0
            name = []
            characters = int(len(str(Video_folder_path)))
            folderPath = str(Video_folder_path) + '\\'
            for entry in obj:
                if entry.is_dir() or entry.is_file():
                    if entry.is_file:
                        name = [entry.name, str(ids)]
                        all_files.append(name)
                        ids+=1

            video_path_to_file = Video_folder_path[len(os.getcwd()):]+'\\'
            return render_template('video.html', files = all_files, path= video_path_to_file)

    elif(request.method == 'GET'):
        global Video_fileToDelete
        os.chdir('static')
        directories = os.listdir()
        ToBeOrganize = True
        for dirs in directories:
            if (dirs == "VideosToOrganize"):
                ToBeOrganize = False
        if ToBeOrganize:
            os.mkdir('VideosToOrganize')
        os.chdir("../")

        if Video_fileToDelete != 0:
            os.remove(Video_fileToDelete)
            Video_fileToDelete = 0
        if video_tmpPath != "":
            Video_folder_path = video_tmpPath
        else:
            Video_folder_path = os.getcwd() + "\static\VideosToOrganize\\"
        obj = os.scandir(Video_folder_path)
        all_files = []
        ids = 0
        name = []
        characters = int(len(str(Video_folder_path)))
        folderPath = str(Video_folder_path) + '\\'
        for entry in obj:
            if entry.is_dir() or entry.is_file():
                if entry.is_file:
                    name = [entry.name, str(ids)]
                    all_files.append(name)
                    ids+=1

        video_path_to_file = Video_folder_path[len(os.getcwd()):]+'\\'
        return render_template('video.html', files = all_files, path= video_path_to_file)

@OrganizerApp.route('/ActionOnVideoMedia', methods=['GET', 'POST'])
def ActionOnVideoMedia_route():
    global video_path_to_file
    if(request.method  == 'POST'):
        cwd =  os.getcwd()
        os.chdir('static')
        Vdirectories = os.listdir()
        VideoOrganized = True
        for Vdirs in Vdirectories:
            if (Vdirs == "Videos_Organized"):
                VideoOrganized = False
        if VideoOrganized:
            os.mkdir('Videos_Organized')
        os.chdir('Videos_Organized')
        Vdirectories = os.listdir()
        Per = True
        Pub = True
        Fam = True
        Mix = True
        GFV = True
        GPB = True
        for Vdirs in Vdirectories:
            if Vdirs == "PER":
                Per = False
            elif Vdirs == "PUB":
                Pub = False
            elif Vdirs == "FAM":
                Fam = False
            elif Vdirs == "MIX":
                Mix = False
            elif Vdirs == "GFV":
                GFV = False
            elif Vdirs == "GPB":
                GPB = False
        if Per:
            os.mkdir('PER')
        if Pub:
            os.mkdir('PUB')
        if Fam:
            os.mkdir("FAM")
        if Mix:
            os.mkdir('MIX')
        if GFV:
            os.mkdir("GFV")
        if GPB:
            os.mkdir("GPB")
        os.chdir("../../")
        VideoActionToDo = request.form['actionOnFile']
        VideoFileToApply = request.form['FileToApply']
        NewVideoName = request.form['name']
        global Video_fileToDelete
        getcwdir = os.getcwd()
        if VideoActionToDo == 'PER':
            shutil.copy(getcwdir + video_path_to_file + VideoFileToApply , getcwdir + '\static\Videos_Organized\PER\\' + VideoFileToApply)
            if NewVideoName != "":
                os.rename(getcwdir + '\static\Videos_Organized\PER\\' + VideoFileToApply , getcwdir + '\static\Videos_Organized\PER\\' + NewVideoName + VideoFileToApply[-4:])
            Video_fileToDelete = getcwdir+ video_path_to_file + VideoFileToApply
            return redirect('/Video')
        elif VideoActionToDo == 'PUB':
            shutil.copy(getcwdir + video_path_to_file + VideoFileToApply , getcwdir + '\static\Videos_Organized\PUB\\' + VideoFileToApply)
            if NewVideoName != "":
                os.rename(getcwdir + '\static\Videos_Organized\PUB\\' + VideoFileToApply , getcwdir + '\static\Videos_Organized\PUB\\' + NewVideoName + VideoFileToApply[-4:])
            Video_fileToDelete = getcwdir+ video_path_to_file + VideoFileToApply
            return redirect('/Video')
        elif VideoActionToDo == 'FAM':
            shutil.copy(getcwdir + video_path_to_file + VideoFileToApply , getcwdir + '\static\Videos_Organized\FAM\\' + VideoFileToApply)
            if NewVideoName != "":
                os.rename(getcwdir + '\static\Videos_Organized\FAM\\' + VideoFileToApply , getcwdir + '\static\Videos_Organized\FAM\\' + NewVideoName + VideoFileToApply[-4:])
            Video_fileToDelete = getcwdir+ video_path_to_file + VideoFileToApply
            return redirect('/Video')
        elif VideoActionToDo == 'MIX':
            shutil.copy(getcwdir + video_path_to_file + VideoFileToApply , getcwdir + '\static\Videos_Organized\MIX\\' + VideoFileToApply)
            if NewVideoName != "":
                os.rename(getcwdir + '\static\Videos_Organized\MIX\\' + VideoFileToApply , getcwdir + '\static\Videos_Organized\MIX\\' + NewVideoName + VideoFileToApply[-4:])
            Video_fileToDelete = getcwdir+ video_path_to_file + VideoFileToApply
            return redirect('/Video')
        elif VideoActionToDo == 'GFV':
            shutil.copy(getcwdir + video_path_to_file + VideoFileToApply , getcwdir + '\static\Videos_Organized\GFV\\' + VideoFileToApply)
            if NewVideoName != "":
                os.rename(getcwdir + '\static\Videos_Organized\GFV\\' + VideoFileToApply , getcwdir + '\static\Videos_Organized\GFV\\' + NewVideoName + VideoFileToApply[-4:])
            Video_fileToDelete = getcwdir+ video_path_to_file + VideoFileToApply
            return redirect('/Video')
        elif VideoActionToDo == 'GPB':
            shutil.copy(getcwdir + video_path_to_file + VideoFileToApply , getcwdir + '\static\Videos_Organized\GPB\\' + VideoFileToApply)
            if NewVideoName != "":
                os.rename(getcwdir + '\static\Videos_Organized\GPB\\' + VideoFileToApply , getcwdir + '\static\Videos_Organized\GPB\\' + NewVideoName + VideoFileToApply[-4:])
            Video_fileToDelete = getcwdir+ video_path_to_file + VideoFileToApply
            return redirect('/Video')
        elif VideoActionToDo == 'DEL':
            os.remove(getcwdir + video_path_to_file + VideoFileToApply)
            return redirect('/Video')







OrganizerApp.run(host="desktop-r230fo4", port=3000,debug=False)