import gradio as gr

class Song:
    type='music'
    def __init__(self, name, artist, length, energy):
        self.name = name
        self.artist = artist
        self.length = length
        self.erg = energy


n=[]
m=[]
sample=[]
sample_art_song=[]
sample_enr=[]
sample_ln=[]


## creates seperate lists I can use later in order to manage 
def collect_songs(sog, art, ln, enr):
    ## message to give if input is valid ot invalid
    message = ""
    z=0
    z=Song(sog, art, ln, enr)
    if z.length > 0 and 100 >= z.erg >= 0 and z.artist != "" and z.name != "" and z.erg != None and z.length!=None:
        sample.append(z)
        sample_art_song.append(f"{z.name}-{z.artist}")
        sample_enr.append(z.erg)
        sample_ln.append(z.length)

        message = "[added to playlist]"
    else:
        message = "[error, invalid input]"
    return (f"{message.upper()}, Song Name/Artist: {sample_art_song}, Song Length: {sample_ln}, Song Energy: {sample_enr}")

def clear_songs():
    sample.clear()
    sample_art_song.clear()
    sample_enr.clear()
    sample_ln.clear()
    return ("playlist cleared")

## 20 song playlist sample
def sample_playlist():
    ## remove previous songs
    clear_songs()
    ## song list
    collect_songs("love me do","beatles",120,30)
    collect_songs("smells like teen spirit", "nirvanna", 157, 71)
    collect_songs("moonage daydream", "david bowie", 310, 32)
    collect_songs("feel good inc", "gorillaz", 100, 43)
    collect_songs("humility", "gorillaz", 84, 21)
    collect_songs("in a jar","dinosaur jr", 150, 65)
    collect_songs("hurt", "johnny cash", 50,3)
    collect_songs("waters of march", "elis regina", 210, 52)
    collect_songs("ahead by a century", "tragically hip", 134, 37)
    collect_songs("sunday candy", "nico segal",105,68)
    collect_songs("sugar on my tongue", "tyler the creator", 87, 76)
    collect_songs("young","little simz",207,49)
    collect_songs("thief", "little simz", 273,68)
    collect_songs("najubes", "love sick pt1", 386,22)
    collect_songs("najubes", "love sick pt2", 234,54)
    collect_songs("najubes", "love sick pt3", 265,40)
    collect_songs("najubes", "love sick pt4", 182,32)
    collect_songs("najubes", "love sick pt5", 201,33)
    collect_songs("kglw","gamma knife",121, 68)
    collect_songs("kglw","witchcraft",254,78)
    collect_songs("brisk","chd", 243, 90)
    

    return (f"[SAMPLE PLAYLIST], Song Name/Artist: {sample_art_song}, Song Length: {sample_ln}, Song Energy: {sample_enr}")

## checks if a step is the one requested and shows it 
def keep_track(playlist_1, playlist_2, type):

    name_art_1 = []
    energy_1 = []
    lenth_1 = []

    name_art_2 = []
    energy_2 = []
    lenth_2 = []
    
    for x in playlist_1:
        name_art_1.append(f"{x.name}-{x.artist}")
        energy_1.append(x.erg)
        lenth_1.append(x.length)
    if type == "split":
        for y in playlist_2:
            name_art_2.append(f"{y.name}-{y.artist}")
            energy_2.append(y.erg)
            lenth_2.append(y.length)
        return(f"{type.upper()}, SONGS/NAMES: {name_art_1} / {name_art_2}, LENGTH: {lenth_1} / {lenth_2}, ENERGY {energy_1} / {energy_2}")
    elif type == "merge":
        return(f"{type.upper()}, SONGS/NAMES: {name_art_1}, LENGTH: {lenth_1}, ENERGY {energy_1}")

## have to call one of these to after pressing a button as I cannot set a button to look for energy with an external variable
def run_program_len(track):
    return run_program(track, "length")

def run_program_enr(track):
    return run_program(track, "energy")

## both functions merge here and return me either the sorted algorthm or the step im looking for
def run_program(track,looking):
            m.clear()
            ## edge case to make sure they dont loop back around the list
            if track < 1:
                return ("invalid step number")
            if len(sample) > 1:
                n = merge_sort(sample, [], [], looking)
                if track >= len(m):
                    return f"SORTED! {m[-1]}"
                else:
                    return m[track-1]
            else:
                return ("add more songs to playlist")


## merge_sort function
def merge_sort(playlist, list_1, list_2,search):
    mid = len(playlist)//2
    print(search)

    ## split in half
    if len(playlist) > 2:
        list_1 = playlist[0:mid]
        list_2 = playlist[mid:len(playlist)]

    elif len(playlist)==2:
        list_1 = [playlist[0]]
        list_2 = [playlist[1]]
    m.append(keep_track(list_1,list_2,"split"))

    ## if not a single element long keep splitting
    print(list_2)
    if len(list_1) > 1:
        list_1=merge_sort(list_1, [], [], search)
    if len(list_2) > 1:
        list_2=merge_sort(list_2, [], [], search)
    
    ## sort elements
    playlist = merge(list_1, list_2,search)
    return playlist

## seperate function so I can call when either comparing energy or length
def left_overs(playlist,remaing):
    for x in remaing:
            playlist.append(x)
    return playlist


## two functions, one to compare length, one to compare length, one to compare to compare energy, both call left_overs()
def compare_energy(playlist_1, playlist_2):

    n=[]
    while playlist_1!=[] or playlist_2!=[]:
        if playlist_1[0].erg <= playlist_2[0].erg:

            n.append(playlist_1.pop(0)) 
            if playlist_1 == []:
                break
        

        if playlist_1[0].erg > playlist_2[0].erg:

            n.append(playlist_2.pop(0))
            if playlist_2 == []:
                break 
    
    ## deal with leftovers
    if playlist_1 != []:
        n = left_overs(n,playlist_1)
    
    elif playlist_2 != []:
        n = left_overs(n,playlist_2)
    
    return n

def compare_length(playlist_1,playlist_2):
    n=[]
    while playlist_1!=[] or playlist_2!=[]:
        if playlist_1[0].length <= playlist_2[0].length:

            n.append(playlist_1.pop(0)) 
            if playlist_1 == []:
                break
        

        if playlist_1[0].length > playlist_2[0].length:

            n.append(playlist_2.pop(0))
            if playlist_2 == []:
                break 
    
    ## deal with leftovers
    if playlist_1 != []:
        n = left_overs(n,playlist_1)
    
    elif playlist_2 != []:
        n = left_overs(n,playlist_2)
    return n


## merging two lists together
def merge(playlist_1, playlist_2,search):

    if search == 'energy':
        n = compare_energy(playlist_1, playlist_2)
    elif search == 'length':
        n = compare_length(playlist_1,playlist_2)
    ## keep track of merges for callbacks later
    m.append(keep_track(n,[],"merge"))

    return n

## gradio
with gr.Blocks() as demo:

    ## adding to playlists
    with gr.Tab("create playlist"):
        ## enter playlist
        gr.Markdown("""
                    ## ENTER PLAYLIST
                    please enter the song names, artist, lengths(second) and excitment levels (0-100) for each of the songs in your playlist""")
    
        with gr.Row():
            temp_song = gr.Textbox(label="song name")
            temp_art = gr.Textbox(label="artist")
            temp_len = gr.Number(label = "length (seconds)")
            temp_enr = gr.Number(label="energy")

    ## adds songs and clears songs in playlist
        with gr.Row():
            with gr.Column():
                add = gr.Button("add to playlist")
                clear = gr.Button("clear playlist")
                sample_btn = gr.Button("20 song sample playlist")

    ##tab 1 output here
            with gr.Column():
                output_1=gr.Textbox(lines=4)

        add.click(collect_songs, inputs=[temp_song, temp_art, temp_len, temp_enr], outputs=output_1)
        clear.click(clear_songs, outputs=output_1)
        sample_btn.click(sample_playlist, outputs=output_1)

    ## second tab for the actual sorting algorthm
    with gr.Tab("sorted"):
        gr.Markdown("""
                        ## MERGE SORT
                        merge sort is a divide and conquer sorting algorthm, input the step below
                        you want view (step must be greater than one) and then click the "sort by energy" or "sort by length" button to see what that step has in store
                        whether its splitting a given list in half or merging to halves together to create a sotred list for either length or energy
                        ### Note: if you go beyond the last step number it will only give you the sorted algorthm""")

        output_2=gr.Textbox(lines=9)
        with gr.Row():
            with gr.Column():
                sort_len = gr.Button("sort by length")
            with gr.Column():
                sort_enr = gr.Button("sort by energy")

        step = gr.Number(label="input step Number")
        sort_len.click(run_program_len, inputs=[step],outputs=output_2)
        sort_enr.click(run_program_enr, inputs=[step],outputs=output_2)

demo.launch()






