package main

import (
	"context"
	"fmt"
	"global"
	"log"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

var client *mongo.Client

type Student struct {
	Name string
	Age  int
}

func initDB() (err error) {
	// 设置客户端连接配置
	clientOptions := options.Client().ApplyURI("mongodb://0.0.0.0:27017")
	// 连接到MongoDB
	client, err = mongo.Connect(context.TODO(), clientOptions)
	if err != nil {
		return err
	}
	// 检查连接
	err = client.Ping(context.TODO(), nil)
	if err != nil {
		return err
	}
	test_collection := client.Database("quant_info").Collection("ag2302")

	cur, err := test_collection.Find(context.TODO(), bson.D{{}})
	if err != nil {
		log.Fatal(err)
	}

	// 查找多个文档返回一个光标
	// 遍历游标允许我们一次解码一个文档
	for cur.Next(context.TODO()) {
		// 创建一个值，将单个文档解码为该值
		var elem global.Tick_info
		err := cur.Decode(&elem)
		if err != nil {
			log.Fatal(err)
		}
		t, _ := time.ParseInLocation("20060102 15:04:05", elem.Time[:17], time.Local)
		fmt.Println(t.Before(time.Now()))
		fmt.Println(elem.Time)
	}

	// s1 := Student{"小红", 12}
	// insertResult, err := test_collection.InsertOne(context.TODO(), s1)
	// if err != nil {
	// 	log.Fatal(err)
	// }

	// fmt.Println("Inserted a single document: ", insertResult.InsertedID)

	return nil
}

func main() {
	err := initDB() // 调用输出化数据库的函数
	if err != nil {
		fmt.Printf("初始化失败！,err:%v\n", err)
		return
	} else {
		fmt.Println("Connected to MongoDB!")
	}
}
