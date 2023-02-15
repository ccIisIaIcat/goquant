package fake

import (
	"context"
	"errors"
	"global"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

// 用于从mongo中查询数据并输出模拟数据流
type FakeQueryMongo struct {
	Query_list     []string // 合约名称列表
	Database_name  string   // 数据库名称
	Tick_info_chan chan global.Tick_info
	Period         int // 两次信息发送间隔毫秒数
	local_database *mongo.Database
}

func (F *FakeQueryMongo) Init() {
	// 端口检查
	if cap(F.Tick_info_chan) == 0 {
		panic(errors.New("missing Tick_info_chan"))
	}
	// 连接到MongoDB
	clientOptions := options.Client().ApplyURI("mongodb://0.0.0.0:27017")

	client, err := mongo.Connect(context.TODO(), clientOptions)
	if err != nil {
		panic(err)
	}
	// 检查连接
	err = client.Ping(context.TODO(), nil)
	if err != nil {
		panic(err)
	}
	F.local_database = client.Database(F.Database_name)

}

func (F *FakeQueryMongo) Start() {
	for i := 0; i < len(F.Query_list); i++ {
		temp_collection := F.local_database.Collection(F.Query_list[i])
		cur, err := temp_collection.Find(context.TODO(), bson.D{{}})
		if err != nil {
			panic(err)
		}
		temp_id := F.Query_list[i]
		go func() {
			for cur.Next(context.TODO()) {
				time.Sleep(time.Millisecond * time.Duration(F.Period))
				// 创建一个值，将单个文档解码为该值
				var elem global.Tick_info
				err := cur.Decode(&elem)
				elem.Ins_id = temp_id
				if err != nil {
					panic(err)
				}
				F.Tick_info_chan <- elem
			}
		}()
	}
}

func (F *FakeQueryMongo) StartBetween(start_time map[string]time.Time, end_time map[string]time.Time) {
	if (len(start_time) != len(end_time)) || (len(start_time) != len(F.Query_list)) {
		panic(errors.New("合约长度和时间点长度不匹配"))
	}
	for i := 0; i < len(F.Query_list); i++ {
		temp_collection := F.local_database.Collection(F.Query_list[i])
		cur, err := temp_collection.Find(context.TODO(), bson.D{{}})
		if err != nil {
			panic(err)
		}
		temp_id := i
		go func() {
			for cur.Next(context.TODO()) {
				// 创建一个值，将单个文档解码为该值
				var elem global.Tick_info
				elem.Ins_id = F.Query_list[temp_id]
				err := cur.Decode(&elem)
				if err != nil {
					panic(err)
				}
				t, _ := time.ParseInLocation("20060102 15:04:05", elem.Time[:17], time.Local)
				if t.After(start_time[F.Query_list[temp_id]]) && t.Before(end_time[F.Query_list[temp_id]]) {
					time.Sleep(time.Millisecond * time.Duration(F.Period))
					F.Tick_info_chan <- elem
				}

			}
		}()
	}
}
