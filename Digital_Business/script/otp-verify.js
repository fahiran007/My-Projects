let otp_verify_label = document.getElementById('otp_status')
if (otp_verify_label.innerText == 'Invalid') {
    otp_verify_label.innerText = 'OTP Code Is Invalid'
    otp_verify_label.style.color = 'red'
    otp_verify_label.style.fontWeight = 'bold'
    otp_verify_label.classList.remove("dis-none")
}