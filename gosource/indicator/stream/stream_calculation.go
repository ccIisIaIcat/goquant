package stream

import "math"

type StreamCalculation struct {
	Data      []float64
	MaxLength int
	////
	data_sqr  []float64
	value_sum float64
	sqr_sum   float64
}

func (S *StreamCalculation) Init() {
	S.data_sqr = make([]float64, 0)
	for i := 0; i < len(S.Data); i++ {
		S.data_sqr = append(S.data_sqr, S.Data[i]*S.Data[i])
	}

	for i := 0; i < len(S.Data); i++ {
		S.value_sum += S.Data[i]
		S.sqr_sum += S.data_sqr[i]
	}

}

func (S *StreamCalculation) Update(num float64) {
	// data
	if len(S.Data) < S.MaxLength {
		S.value_sum += num
		S.sqr_sum += num * num

		// 更新数据集
		S.Data = append(S.Data, num)
		S.data_sqr = append(S.data_sqr, num*num)
	} else {
		S.value_sum += num
		S.sqr_sum += num * num
		S.value_sum -= S.Data[0]
		S.sqr_sum -= S.data_sqr[0]

		// 更新数据集
		S.Data = append(S.Data, num)
		S.data_sqr = append(S.data_sqr, num*num)
		S.Data = S.Data[1:]
		S.data_sqr = S.data_sqr[1:]
	}
}

func (S *StreamCalculation) Mean() float64 {
	return S.value_sum / float64(len(S.Data))
}

func (S *StreamCalculation) Variance() float64 {
	return S.value_sum/float64(len(S.Data)) - (S.value_sum/float64(len(S.Data)))*(S.value_sum/float64(len(S.Data)))
}

func (S *StreamCalculation) Std() float64 {
	return math.Sqrt(S.value_sum/float64(len(S.Data)) - (S.value_sum/float64(len(S.Data)))*(S.value_sum/float64(len(S.Data))))
}
