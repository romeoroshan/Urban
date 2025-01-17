
        $(document).ready(function () {
            $("#fn").keyup(function () {
                validateName("#fn");
            });
            $("#ln").keyup(function () {
                validateName("#ln");
            });

            $("#sn").keyup(function () {
                validateName2("#sn");
            });

            $("#mail").keyup(function () {
                validateEmail("#mail");
            });

            $("#pass").keyup(function () {
                validatePassword("#pass");
            });

            $("#cpass").keyup(function () {
                validateConfirmPassword("#cpass");
            });

            $("#phone").keyup(function () {
                console.log("Keyup")
                validatePhoneNumber("#phone");
            });
            $('#dateofbirth').change(function(){
                TDate();
            });
        });

        function validateName(fieldId) {
            var name = $(fieldId).val();
            console.log(name);
            var submit = document.getElementById("submit_button");
            console.log(submit);
            var lettersWithSpaces = /^[A-Za-z\s]+$/;
        
            if (name.trim() === "") {
                console.log("entered");
                $("#fname").html("Enter the Name").css("color", "red");
                submit.disabled = true;
            } else if (!lettersWithSpaces.test(name)) {
                // Use the disabled property directly
                submit.disabled = true;
                $("#fname").html("Name field required only alphabet characters with spaces").css("color", "red");
            } else {
                $("#fname").html("");
                // Re-enable the button if needed
                submit.disabled = false;
                $(".submit-btn")
            }
        }
        

        function validateName2(fieldId) {
            var name = $(fieldId).val();
            console.log(name);
            var submit = document.getElementById("submit_button");
            var para=document.getElementById("fname");
            console.log(para)
            console.log(submit);
            var lettersWithSpaces = /^[A-Za-z\s]+$/;
        
            if (name.trim() === "") {
                console.log("entered");
                para.html("Enter the Name").css("color", "red");
                submit.disabled = true;
            } else if (!lettersWithSpaces.test(name)) {
                // Use the disabled property directly
                submit.disabled = true;
                para.html("Name field required only alphabet characters with spaces").css("color", "red");
            } else {
                para.html("");
                // Re-enable the button if needed
                submit.disabled = false;
                $(".submit-btn")
            }
        }


        function validateEmail(fieldId) {
            var email = $(fieldId).val();
            var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
            if (email === "") {
                $("#email").html("Enter the Email Id").css("color", "red");
            } else if (!filter.test(email)) {
                $("#email").html("Use correct Email Id").css("color", "red");
            } else {
                $("#email").html("");
            }
        }

        function validatePassword(fieldId) {
            var password = $(fieldId).val();
            var pwd_expression = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])/;
            if (password === "") {
                $("#pass1").html("Enter the Password").css("color", "red");
            }else if(!pwd_expression.test(password))
                    {
                        $("#pass1").html("Use password with atleast one capital and small alphabets, special character and letters").css("color", "red");
                    }
            else 
            {
                $("#pass1").html("");
            }
        }

        function validateConfirmPassword(fieldId) {
            var password = $("#pass").val();
            var confirmPassword = $(fieldId).val();
            if (confirmPassword === "") {
                $("#cpass1").html("Enter the Confirm Password").css("color", "red");
            } else if (confirmPassword !== password) {
                $("#cpass1").html("Password do not match").css("color", "red");
            } else {
                $("#cpass1").html("");
            }
        }

        function validatePhoneNumber(fieldId) {
            console.log("Entered")
            var numberRegex = /^[-+]?\d*\.?\d+$/;
            var phoneNumber = $(fieldId).val();

            if (phoneNumber === "") {
                $("#phone1").html("Enter the Phone number").css("color", "red");
            } else if (!numberRegex.test(phoneNumber)) {
                $("#phone1").html("Invalid phone Number").css("color", "red");
            } else if (phoneNumber.length > 10) {
                $("#phone1").html("The phone number should have 10 numbers").css("color", "red");
            }
            else if (phoneNumber.length < 10) {
                $("#phone1").html("The phone number should have 10 numbers").css("color", "red");
            }
            else {
                $("#phone1").html("");
            }
        }


        function togglePasswordVisibility() {
            var passwordInput = document.getElementById("pass");
            var eyeIcon = document.getElementById("eyeIcon");

            if (passwordInput.type === "password") {
                passwordInput.type = "text";
                eyeIcon.classList.remove("fa-eye-slash");
                eyeIcon.classList.add("fa-eye");
            } else {
                passwordInput.type = "password";
                eyeIcon.classList.remove("fa-eye");
                eyeIcon.classList.add("fa-eye-slash");
            }
        }
        function togglecPasswordVisibility() {
            var passwordInput = document.getElementById("cpass");
            var eyeIcon = document.getElementById("eyeIcon2");

            if (passwordInput.type === "password") {
                passwordInput.type = "text";
                eyeIcon.classList.remove("fa-eye-slash");
                eyeIcon.classList.add("fa-eye");
            } else {
                passwordInput.type = "password";
                eyeIcon.classList.remove("fa-eye");
                eyeIcon.classList.add("fa-eye-slash");
            }
        }

        function TDate() {
            console.log("Working");
            var UserDate = document.getElementById("dateofbirth").value;
            var UserDate = new Date(UserDate);
            var ToDate = new Date(2016, 0, 1); 
            console.log(ToDate>UserDate) // Changed month to 0 (January)
            
            if (UserDate>ToDate) {
                $("#dob").html("You must be born before 2016").css("color", "red");
                console.log('in')
                return false;
            }
            return true;
        }
        