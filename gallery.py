from pyscript import document

photos = [
    {"name": "Teachers Day", "desc": "We luv sir Calpo!", "img": "copy of IMG_5349.CR3"}, 
    {"name": "Christmas Party", "desc": "Omg green", "img": "copy of IMG_5708.JPG"}, 
    {"name": "Food Fair", "desc": "Coco to my jam!", "img": "DSC00175.JPG"}, 
]

gallery = document.getElementById("gallery")

html = ""

for p in photos:
    html += f"""
    <div class="card">
        <img src="{p['img']}" alt="{p['name']}">
        <h3>{p['name']}</h3>
        <p>{p['desc']}</p>
    </div>
    """

gallery.innerHTML = html
