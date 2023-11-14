import csv
from datetime import datetime
from django.core.management import BaseCommand
from techs.models import Company, Post, Tag, Post_tag, Company_Tag

class Command(BaseCommand):
    help = 'Load data from CSV file'

    def handle(self, *args, **kwargs):
        with open('데보션.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                company, _ = Company.objects.get_or_create(company_name=row['company'])
                
                post, _ = Post.objects.get_or_create(
                    title=row['\ufefftitle'],
                    company=company,
                    date=datetime.strptime(row['date'], "%Y.%m.%d"),
                    url=row['link'],
                    defaults={'views': 0, 'likes': 0}
                )

                tags = list(row['tags'].split("#"))
                for tag_name in tags:
                    tag, _ = Tag.objects.get_or_create(tag_name=tag_name)
                    
                    Post_tag.objects.get_or_create(
                        post=post,
                        tag=tag,
                    )
                    
                    company_tag, created = Company_Tag.objects.get_or_create(
                        company=company,
                        tag=tag,
                        defaults={'updates': datetime.now()}
                    )
                    
                    if not created:
                        company_tag.updates = datetime.now()
                        company_tag.count += 1
                        company_tag.save()

            
'''
from django.core.management.base import BaseCommand
import pandas as pd
from techs.models import *  # ?��?��?�� 모델
from datetime import datetime

## 주소/management/commands
#  python manage.py load_csv

class Command(BaseCommand):
    help = 'Load data from CSV file into Company model'

    def handle(self, *args, **options):
        df = pd.read_csv('?���?.csv', encoding='utf-8')

        
        for index, row in df.iterrows():
            Company.objects.get_or_create(
                company_name=row['company__name'])
                
            for tag in row['tags']:
                Tag.objects.get_or_create(
                    tag_name = tag
            )
                
            company, _ = Company.objects.get_or_create(company_name = row['company__name'])
            Post.objects.create(
                title=row['title'],
                company_id=company.id,
                date = row['pub_date'],
                views = 0,
                likes = 0,
                url = row['url']
            )

        
            post= Post.objects.get(title = row['title'])
            tag, _ = Tag.objects.get(tag_name=row['tag_name'])
            Post_tag.objects.create(
            Post=post.id,
            tag=tag.id,
            update_date=datetime.now(),
            )
        
            company,  = Company.objects.get_or_create(company_name=row['company__name'])
            tag, _ = Tag.objects.get_or_create(tag_name=row['tag_name'])
            count = Company_Tag.objects.filter(tag=tag).count()
            Company_Tag.objects.create(
                Company=company.id,
                tag=tag.id,
                update_date=datetime.now(),
                Count=count
'''


            

