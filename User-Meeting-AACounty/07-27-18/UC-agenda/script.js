(function() {
    counter = 0
    slideList = document.getElementById('slider').children
    console.log(slideList)
    document.addEventListener("keydown", function(e){
       if (e.key == "ArrowRight") {
				if (counter < slideList.length){
					if (counter > 0 && counter < slideList.length){
						slideList[counter-1].style.display = 'None'
					}
					slideList[counter].style.display = 'block'
					if (counter < slideList.length-1){
						counter += 1
					}
				}
       }
       if (e.key == "ArrowLeft") {
				console.log(counter)
        if (counter > 0){
					slideList[counter].style.display = 'None'
					slideList[counter-1].style.display = 'Block'
					counter -= 1
					}

        }

    })

})()