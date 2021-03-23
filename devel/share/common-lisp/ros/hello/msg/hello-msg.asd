
(cl:in-package :asdf)

(defsystem "hello-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "vision" :depends-on ("_package_vision"))
    (:file "_package_vision" :depends-on ("_package"))
  ))