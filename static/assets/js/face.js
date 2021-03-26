const video = document.getElementById('video')

Promise.all([
    faceapi.nets.tinyFaceDetector.loadFromUri('/static/assets/js/models'),
    // faceapi.nets.faceLandmark68Net.loadFromUri('/static/assets/js/models'),
    faceapi.nets.faceRecognitionNet.loadFromUri('/static/assets/js/models'),
    // faceapi.nets.faceExpressionNet.loadFromUri('/static/assets/js/models')
  ]).then(startVideo)

function startVideo(){
    navigator.getUserMedia(
        { video: {} },
        stream => video.srcObject = stream,
        err => console.error(err) 
    )
}

video.addEventListener('play', () => {
    const canvas = faceapi.createCanvasFromMedia(video)
    document.body.append(canvas)
    const displaySize = { width: video.width, height: video.height }
    faceapi.matchDimensions(canvas, displaySize)
    setInterval(async () => {
        const detections = await faceapi.detectSingleFace(video, 
            new faceapi.TinyFaceDetectorOptions({
                minConfidence: 0.80,
                maxResults: 1
            })
        )//.withFaceLandmarks().withFaceExpressions() //detectMultipleFaces
        const resizedDetections = faceapi.resizeResults(detections, displaySize)
        canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
        faceapi.draw.drawDetections(canvas, resizedDetections)
        // faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
        // faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
    }, 500)
})