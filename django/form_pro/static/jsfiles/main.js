console.log('hello world')
const alertBox = document.getElementById('alert-box')
const imageBox = document.getElementById('image-box')
const imageForm = document.getElementById('image-form')
const confirmBtn = document.getElementById('confirm-btn')
const input = document.getElementById('id_file')
p = document.getElementById('prev')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

$(document).find('input').change((e) => {
    //    p.removeClass('d-none')
    alertBox.innerHTML = ""
    confirmBtn.classList.remove('not-visible')
    const img_data = input.files[0]
    const url = URL.createObjectURL(img_data)

    imageBox.innerHTML = `<img src="${url}" id="image" width="700px">`
    var $image = $('#image')
    console.log($image)

    $image.cropper({
        aspectRatio: 16 / 9,
        crop: function (event) {
            console.log(event.detail.x);
            console.log(event.detail.y);
            console.log(event.detail.width);
            console.log(event.detail.height);
            console.log(event.detail.rotate);
            console.log(event.detail.scaleX);
            console.log(event.detail.scaleY);
        }
    });

    document.getElementById('preview-btn').addEventListener('click', (e) => {

        cropper.getCroppedCanvas().toBlob((blob) => {
            console.log('confirmed')
            const fd = new FormData();
            fd.append('csrfmiddlewaretoken', csrf[0].value)
            fd.append('file', blob, 'my-image.png');
            console.log(fd.get('file')['name'])
            u = window.URL.createObjectURL(fd.get('file'))
            console.log(u)
            document.getElementsByClassName('preview')[0].setAttribute("src", u);
        })
    })

    var cropper = $image.data('cropper');
    confirmBtn.addEventListener('click', () => {
        cropper.getCroppedCanvas().toBlob((blob) => {
            console.log('confirmed')
            const fd = new FormData();
            fd.append('csrfmiddlewaretoken', csrf[0].value)
            fd.append('file', blob, 'my-image.png');
            console.log(fd.get('file'), 'ffffffddddddddddd')
            $.ajax({
                type: 'POST',
                url: imageForm.action,
                enctype: 'multipart/form-data',
                data: fd,
                success: function (response) {
                    console.log('success', response, '--------------')
                    if (response == true) {
                        setTimeout(function () {
                            window.location.href = "/view"
                        }, 3000)

                        toastr.success(response.msg + " Redirecting back to home.")
                    }
                    alertBox.innerHTML = `<div class="alert alert-success" role="alert">
                                          Successfully saved and cropped the selected image
                                      </div>`
                },
                error: function (error) {
                    console.log('error', error)
                    alertBox.innerHTML = `<div class="alert alert-danger" role="alert">
                                          Ups...something went wrong
                                      </div>`
                },
                cache: false,
                contentType: false,
                processData: false,
            })
        })
    })
})
