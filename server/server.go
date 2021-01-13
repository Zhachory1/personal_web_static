package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		log.Printf("Grabbing %s", r.URL.Path[1:])
        http.ServeFile(w, r, r.URL.Path[1:])
    })

	http.HandleFunc("/hi", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hi")
		log.Printf("Said hi for %s", r.RemoteAddr)
	})

	log.Print("Now serving on localhost:8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}