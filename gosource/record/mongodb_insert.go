package record

import (
	"context"
	"global"

	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type Mongodb_obj struct {
	Tick_info_chan chan global.Tick_info
	Database_name  string
	local_database *mongo.Database
}

func (M *Mongodb_obj) Init() {
	if cap(M.Tick_info_chan) == 0 {
		panic("missing Tick_info_chan")
	}
	if M.Database_name == "" {
		panic("missing Database")
	}
	clientOptions := options.Client().ApplyURI("mongodb://0.0.0.0:27017")
	// 连接到MongoDB
	client, err := mongo.Connect(context.TODO(), clientOptions)
	if err != nil {
		panic(err)
	}
	// 检查连接
	err = client.Ping(context.TODO(), nil)
	if err != nil {
		panic(err)
	}
	M.local_database = client.Database(M.Database_name)
}

func (M *Mongodb_obj) InsertByTick() {
	for {
		t_price := <-M.Tick_info_chan
		M.local_database.Collection(t_price.Ins_id).InsertOne(context.TODO(), t_price)
	}

}
