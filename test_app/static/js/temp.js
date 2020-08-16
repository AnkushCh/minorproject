
    window.onload = function(){
        document.getElementById('subject').selectedIndex = -1;
      }

      /*
document.onkeydown = function (e) {
    return false;
}
*/

function logKey(e) { 
    if(e.code === "esc"){
    // do something
    window.alert('Do not exit full screen before completing test')
    }
    }
    /* Get the documentElement (<html>) to display the page in fullscreen */
        var elem = document.documentElement;
        function resize(){
            window.moveTo(0, 0);
            window.resizeTo(screen.width, screen.height)
        }
        /* View in fullscreen */
        function openFullscreen() {
        
        if (elem.requestFullscreen) {
            elem.requestFullscreen();
        } else if (elem.mozRequestFullScreen) { /* Firefox */
            elem.mozRequestFullScreen();
        } else if (elem.webkitRequestFullscreen) { /* Chrome, Safari and Opera */
            elem.webkitRequestFullscreen();
        } else if (elem.msRequestFullscreen) { /* IE/Edge */
            elem.msRequestFullscreen();
        }
        }
    
    
        /* Close fullscreen */
        function closeFullscreen() {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        } else if (document.mozCancelFullScreen) { /* Firefox */
            document.mozCancelFullScreen();
        } else if (document.webkitExitFullscreen) { /* Chrome, Safari and Opera */
            document.webkitExitFullscreen();
        } else if (document.msExitFullscreen) { /* IE/Edge */
            document.msExitFullscreen();
        }
        }
    
        function closeWin() {
            window.open('','_parent','');
            window.close();
        }