package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	http.Handle("/", http.FileServer(http.Dir("public")))

	http.HandleFunc("/hi", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hi")
		log.Print("Said hi for %s", r.RemoteAddr)
	})

	log.Print("Now serving on localhost:8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}