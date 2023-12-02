import { Component, OnInit } from '@angular/core';
import { NewsItem } from '../model/newsitem';
import { NewsService } from '../service/news.service';

@Component({
  selector: 'app-news-items',
  templateUrl: './news-items.component.html',
  styleUrls: ['./news-items.component.css']
})
export class NewsItemsComponent implements OnInit {
  country: string = 'in'
  category: string = 'business'
  page: number = 1
  newsItems: NewsItem[] = [];
  constructor(private newsService: NewsService) { }

  nextpage() {
    this.page = this.page + 1
    this.loadNewItems()
  }

  prevpage() {
    if (this.page > 1) {
      this.page = this.page - 1
      this.loadNewItems()
    }
  }

  ngOnInit(): void {
    this.loadNewItems();
  }

  loadNewItems() {
    this.newsService.getTopNewsItems(this.category, this.country, this.page).subscribe((data: any) => {
      this.newsItems = []
      data.articles.forEach((element: any) => {
        let newsItem: NewsItem = {
          title: element.title,
          description: element.description,
          url: element.url,
          urlToImage: element.urlToImage
        };
        this.newsItems.push(newsItem)
      });
    });
  }

}
