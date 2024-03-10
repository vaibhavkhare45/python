from stegano import lsb

secret_message =lsb.hide("bgmi.jpg", "aaja bhai game me")
secret_message.save("bgmi")