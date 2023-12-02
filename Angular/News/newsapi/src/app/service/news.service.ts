import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { NewsItem } from '../model/newsitem';
import { Observable,of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NewsService {

  constructor(private httpClient:HttpClient) { }

  getTopNewsItems(category:string,country:string,page:number){
    let newsItems:NewsItem[]=[];
    let url = `https://newsapi.org/v2/top-headlines?country=${country}&category=${category}&pageSize=5&page=${page}&apiKey=2ee1c7bb9d31470fb388358b0bc41d27`
    return this.httpClient.get(url)
  }
}

